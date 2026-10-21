from agent.models import DeviceInfo

def test_device_info():
    device = DeviceInfo(
        hostname="DESKTOP-001",
        os_name="Windows",
        os_release="11",
        os_version="10.0.26100",
        architecture="AMD64",
        processor="AMD Ryzen 9",
        logical_cores=16,
        total_gb_ram=32.0,
        total_disk_gb=1000.0,
        used_disk_gb=400.0,
        free_disk_gb=600.0,
        disk_percent_used=40.0,
        last_boot="2026-10-20 08:30:00",
        uptime_seconds=86400,
        uptime_days=1,
        uptime_hours=0,
        uptime_minutes=0
    )

    assert isinstance(device, DeviceInfo)
    assert device.hostname == "DESKTOP-001"
    assert device.total_gb_ram == 32.0
    assert device.uptime_seconds == 86400

    device.logical_cores = None
    assert device.logical_cores is None