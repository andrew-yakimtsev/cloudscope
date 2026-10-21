from agent.system_info import get_system_info, get_disk_info, get_uptime_info

def test_get_system_info():
    system_info = get_system_info()

    assert isinstance(system_info, dict)
    assert "hostname" in system_info
    assert "os_name" in system_info
    assert "os_release" in system_info
    assert "os_version" in system_info
    assert "architecture" in system_info
    assert "processor" in system_info
    assert "logical_cores" in system_info
    assert "total_gb_ram" in system_info
    assert isinstance(system_info["total_gb_ram"], float)

def test_get_disk_info():
    disk_info = get_disk_info()

    assert isinstance(disk_info, dict)
    assert isinstance(disk_info["total_disk_gb"], float)
    assert isinstance(disk_info["used_disk_gb"], float)
    assert isinstance(disk_info["free_disk_gb"], float)
    assert isinstance(disk_info["disk_percent_used"], float)

def test_get_uptime_info():
    uptime_info = get_uptime_info()

    assert isinstance(uptime_info, dict)
    assert isinstance(uptime_info["last_boot"], str)
    assert isinstance(uptime_info["uptime_seconds"], int)
    assert isinstance(uptime_info["uptime_days"], int)
    assert isinstance(uptime_info["uptime_hours"], int)
    assert isinstance(uptime_info["uptime_minutes"], int)

    assert uptime_info["uptime_seconds"] >= 0
    assert 0 <= uptime_info["uptime_hours"] < 24
    assert 0 <= uptime_info["uptime_minutes"] < 60