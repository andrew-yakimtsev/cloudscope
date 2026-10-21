from dataclasses import dataclass

@dataclass
class DeviceInfo:
    hostname: str
    os_name: str
    os_release: str
    os_version: str
    architecture: str
    processor: str
    logical_cores: int | None
    total_gb_ram: float
    total_disk_gb: float
    used_disk_gb: float
    free_disk_gb: float
    disk_percent_used: float
    last_boot: str
    uptime_seconds: int
    uptime_days: int
    uptime_hours: int
    uptime_minutes: int