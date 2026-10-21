
import agent.collector as collector
from agent.models import DeviceInfo

def test_collect_device_info(monkeypatch):
    system_info = {
        "hostname": "DESKTOP-001",
        "os_name": "Windows",
        "os_release": "11",
        "os_version": "10.0.26100",
        "architecture": "AMD64",
        "processor": "AMD Ryzen 9",
        "logical_cores": 16,
        "total_gb_ram": 32.0
    }

    disk_info = {
        "total_disk_gb": 500.0,
        "used_disk_gb": 200.0,
        "free_disk_gb": 300.0,
        "disk_percent_used": 40.0
    }

    uptime_info = {
        "last_boot": "2026-10-20 08:30:00",
        "uptime_seconds": 86400,
        "uptime_days": 1,
        "uptime_hours": 0,
        "uptime_minutes": 0
    }

    monkeypatch.setattr(collector, "get_system_info", lambda: system_info)
    monkeypatch.setattr(collector, "get_disk_info", lambda: disk_info)
    monkeypatch.setattr(collector, "get_uptime_info", lambda: uptime_info)

    device = collector.collect_device_info()

    assert isinstance(device, DeviceInfo)
    assert device.hostname == "DESKTOP-001"
    assert device.total_disk_gb == 500.0
    assert device.used_disk_gb == 200.0
    assert device.uptime_seconds == 86400
    assert device.uptime_days == 1
    assert set(vars(device)) == set(system_info | disk_info | uptime_info)