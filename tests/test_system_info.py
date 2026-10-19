from agent.system_info import get_system_info, get_disk_info

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