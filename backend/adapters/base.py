from abc import ABC, abstractmethod
from typing import Dict, List, Any

class OSAdapter(ABC):
    """
    Abstract Base Class for OS-specific system operations.
    All platform adapters must implement these methods.
    """

    @abstractmethod
    def get_system_health(self) -> Dict[str, Any]:
        """
        Retrieves current system stats.
        Returns:
            Dict containing cpu_usage, ram_percent, disk_usage, etc.
        """
        pass

    @abstractmethod
    def clean_temp_files(self) -> List[str]:
        """
        Performs a safe cleanup of temporary files.
        Returns:
            List of paths that were successfully cleaned.
        """
        pass

    @abstractmethod
    def set_performance_mode(self, mode: str):
        """
        Adjusts system power/performance settings.
        Args:
            mode: 'battery', 'balanced', or 'turbo'
        """
        pass

    @abstractmethod
    def get_heavy_processes(self, limit: int = 5) -> List[Dict]:
        """
        Identifies processes consuming high resources.
        Args:
            limit: Number of processes to return.
        """
        pass
