import platform, psutil
from datetime import datetime, timezone

def get_system_info():
    system_info = {
        "hostname": platform.node(),
        "os_name": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "architecture": platform.machine(),

        "processor": platform.processor(),
        "logical_cores": psutil.cpu_count(logical=True),
        "total_gb_ram": round(psutil.virtual_memory().total / (1024 ** 3), 2),
    }

    return system_info

def get_disk_info():
    disk = psutil.disk_usage("/")

    disk_info = {
        "total_disk_gb": round(disk.total / (1024 ** 3), 2),
        "used_disk_gb": round(disk.used / (1024 ** 3), 2),
        "free_disk_gb": round(disk.free / (1024 ** 3), 2),
        "disk_percent_used": float(disk.percent)
    }

    return disk_info


def get_uptime_info():
    boot_timestamp = psutil.boot_time()

    last_boot = datetime.fromtimestamp(boot_timestamp)
    current_timestamp = datetime.now(timezone.utc).timestamp()

    uptime_seconds = max(0, int(current_timestamp - boot_timestamp))

    uptime_days, remaining_seconds = divmod(uptime_seconds, 86400)
    uptime_hours, remaining_seconds = divmod(remaining_seconds, 3600)
    uptime_minutes, _ = divmod(remaining_seconds, 60)

    uptime_info = {
        "last_boot": last_boot.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime_seconds": uptime_seconds,
        "uptime_days": uptime_days,
        "uptime_hours": uptime_hours,
        "uptime_minutes": uptime_minutes
    }

    return uptime_info

if __name__ == "__main__":
    for key, value in get_system_info().items():
        print(f"{key}: {value}")

    for key, value in get_disk_info().items():
        print(f"{key}: {value}")

    for key, value in get_uptime_info().items():
        print(f"{key}: {value}")