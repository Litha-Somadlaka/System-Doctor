from typing import List, Dict
try:
    from ..adapters.base import OSAdapter
    from ..adapters.windows import WindowsAdapter
except ImportError:
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
    from adapters.base import OSAdapter
    from adapters.windows import WindowsAdapter
import platform

class ProcessManager:
    def __init__(self):
        self.adapter = self._get_adapter()

    def _get_adapter(self) -> OSAdapter:
        # Simple factory duplication for MVP - Refactor to common factory later
        sys_name = platform.system()
        if sys_name == "Windows":
            return WindowsAdapter()
        return WindowsAdapter() # Fallback for now

    def get_top_processes(self, limit: int = 10) -> List[Dict]:
        return self.adapter.get_heavy_processes(limit)
