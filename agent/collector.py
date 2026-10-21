from agent.system_info import get_system_info, get_disk_info, get_uptime_info
from agent.models import DeviceInfo

def collect_device_info() -> DeviceInfo:
    system_info = get_system_info()
    disk_info = get_disk_info()
    uptime_info = get_uptime_info()

    combined_info = system_info | disk_info | uptime_info
    device_info = DeviceInfo(**combined_info)
    
    return device_info