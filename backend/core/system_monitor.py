import platform
from typing import Dict, Any
# Adjust import based on how we run this (as module vs script)
# For now, assuming run from 'backend' or root with path set
try:
    from ..adapters.base import OSAdapter
    from ..adapters.windows import WindowsAdapter
except ImportError:
    # Fallback for direct execution testing if path issues
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
    from adapters.base import OSAdapter
    from adapters.windows import WindowsAdapter


class SystemMonitor:
    def __init__(self):
        self.adapter: OSAdapter = self._get_adapter()
        # Prime CPU measurement to avoid 0.0 on first call
        try:
            import psutil
            psutil.cpu_percent(interval=None)
        except ImportError:
            pass
        
    def _get_adapter(self) -> OSAdapter:
        sys_name = platform.system()
        if sys_name == "Windows":
            return WindowsAdapter()
        elif sys_name == "Darwin":
            # return MacOSAdapter() # To be implemented
            raise NotImplementedError("macOS not yet linked")
        elif sys_name == "Linux":
            # return LinuxAdapter() # To be implemented
            raise NotImplementedError("Linux not yet linked")
        else:
            raise NotImplementedError(f"Unsupported OS: {sys_name}")

    def get_health_stats(self) -> Dict[str, Any]:
        """
        Public API to get current system health
        """
        return self.adapter.get_system_health()
    
    def run_cleanup(self) -> Dict[str, Any]:
        """
        Executes cleanup and returns report
        """
        cleaned_files = self.adapter.clean_temp_files()
        return {
            "success": True,
            "cleaned_count": len(cleaned_files),
            "details": cleaned_files
        }
