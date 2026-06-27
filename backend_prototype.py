import psutil
import platform
import os
import shutil
import subprocess
from abc import ABC, abstractmethod
from typing import Dict, List, Any

# --- Abstract Base Class for OS Adapters ---
class OSAdapter(ABC):
    @abstractmethod
    def get_system_health(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def clean_temp_files(self) -> List[str]:
        """Returns list of cleaned paths/files"""
        pass

    @abstractmethod
    def set_performance_mode(self, mode: str):
        """Accepted modes: 'battery', 'balanced', 'turbo'"""
        pass

    @abstractmethod
    def get_heavy_processes(self, limit: int = 5) -> List[Dict]:
        pass


# --- Windows Implementation ---
class WindowsAdapter(OSAdapter):
    def get_system_health(self) -> Dict[str, Any]:
        return {
            "os": "Windows",
            "cpu_usage": psutil.cpu_percent(interval=0.1),
            "ram_percent": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage('C:\\').percent
        }

    def clean_temp_files(self) -> List[str]:
        cleaned = []
        temp_dirs = [
            os.environ.get('TEMP'),
            os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')
        ]
        
        for p in temp_dirs:
            if p and os.path.exists(p):
                # Simplified implementation: In real app, check for open locks
                for root, dirs, files in os.walk(p):
                    for f in files:
                        try:
                            fp = os.path.join(root, f)
                            os.remove(fp)
                            cleaned.append(fp)
                        except Exception:
                            pass # Skip locked files
        return cleaned

    def set_performance_mode(self, mode: str):
        # Example using powercfg (requires Admin usually, or user context depends on policy)
        # These GUIDs are standard for Windows
        plans = {
            "battery": "a1841308-3541-4fab-bc81-f71556f20b4a", # Power Saver
            "balanced": "381b4222-f694-41f0-9685-ff5bb260df2e", # Balanced
            "turbo": "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"     # High Performance
        }
        guid = plans.get(mode)
        if guid:
            subprocess.run(["powercfg", "/setactive", guid], shell=True)

    def get_heavy_processes(self, limit: int = 5) -> List[Dict]:
        procs = []
        for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                # Calculate metric (simple CPU + RAM weight)
                mem_mb = p.info['memory_info'].rss / 1024 / 1024
                procs.append({
                    "pid": p.info['pid'],
                    "name": p.info['name'],
                    "cpu": p.info['cpu_percent'],
                    "mem_mb": mem_mb
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Sort by Memory for MVP (CPU requires monitoring over time to be accurate)
        return sorted(procs, key=lambda x: x['mem_mb'], reverse=True)[:limit]


# --- macOS Implementation ---
class MacOSAdapter(OSAdapter):
    def get_system_health(self) -> Dict[str, Any]:
        return {
            "os": "macOS",
            "cpu_usage": psutil.cpu_percent(interval=0.1),
            "ram_percent": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage('/').percent
        }

    def clean_temp_files(self) -> List[str]:
        cleaned = []
        user_cache = os.path.expanduser("~/Library/Caches")
        # Be very careful here in production
        return ["Simulated cleaning of " + user_cache] 

    def set_performance_mode(self, mode: str):
        # macOS doesn't have direct power plans like Windows, but we can manage specific settings
        # or use `pmset` (requires sudo)
        pass

    def get_heavy_processes(self, limit: int = 5) -> List[Dict]:
        return WindowsAdapter.get_heavy_processes(self, limit) 


# --- Factory ---
def get_os_adapter() -> OSAdapter:
    sys = platform.system()
    if sys == "Windows":
        return WindowsAdapter()
    elif sys == "Darwin":
        return MacOSAdapter()
    else:
        # Default to a generic one or raise
        raise NotImplementedError(f"OS {sys} not supported in this prototype")

# --- usage ---
if __name__ == "__main__":
    adapter = get_os_adapter()
    print(f"Health: {adapter.get_system_health()}")
    print("Heavy Processes:")
    for p in adapter.get_heavy_processes():
        print(f" - {p['name']} (PEM: {p['mem_mb']:.1f}MB)")
