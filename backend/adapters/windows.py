import psutil
import os
import subprocess
from typing import Dict, List, Any
from .base import OSAdapter

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
        # Common Windows temp locations
        temp_dirs = [
            os.environ.get('TEMP'),
            os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')
        ]
        
        # Safety: Only delete files older than 24 hours
        import time
        SAFE_AGE_SECONDS = 24 * 60 * 60
        now = time.time()
        
        for p in temp_dirs:
            if p and os.path.exists(p):
                # Walk and delete safe files
                for root, dirs, files in os.walk(p):
                    for f in files:
                        try:
                            fp = os.path.join(root, f)
                            
                            # Check file age
                            stat = os.stat(fp)
                            if now - stat.st_mtime < SAFE_AGE_SECONDS:
                                continue # Skip recent files
                                
                            # Basic safety: don't delete if modified in last minute? 
                            # For MVP, we'll try to delete and catch errors.
                            os.remove(fp)
                            cleaned.append(fp)
                        except (PermissionError, OSError):
                            # Skip locked files silently
                            pass
        return cleaned

    def set_performance_mode(self, mode: str):
        # Mappings to standard Windows Power Scheme GUIDs
        plans = {
            "battery": "a1841308-3541-4fab-bc81-f71556f20b4a", # Power Saver
            "balanced": "381b4222-f694-41f0-9685-ff5bb260df2e", # Balanced
            "turbo": "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"     # High Performance
        }
        guid = plans.get(mode)
        if guid:
            # powercfg usually works without admin for switching ALREADY AVAILABLE plans
            # If the plan doesn't exist, this might fail silently.
            subprocess.run(["powercfg", "/setactive", guid], shell=True)

    def get_heavy_processes(self, limit: int = 5) -> List[Dict]:
        procs = []
        # Iterate over all running processes
        for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                # Calculate Memory in MB
                mem_mb = p.info['memory_info'].rss / 1024 / 1024
                procs.append({
                    "pid": p.info['pid'],
                    "name": p.info['name'],
                    "cpu": p.info['cpu_percent'], # Note: cpu_percent needs interval or previous calls to be accurate
                    "mem_mb": mem_mb
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        # Sort by Memory Usage for MVP stability (CPU effectively requires sampling)
        return sorted(procs, key=lambda x: x['mem_mb'], reverse=True)[:limit]
