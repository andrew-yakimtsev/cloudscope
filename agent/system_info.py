import platform, psutil

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

if __name__ == "__main__":
    for key, value in get_system_info().items():
        print(f"{key}: {value}")

    for key, value in get_disk_info().items():
        print(f"{key}: {value}")