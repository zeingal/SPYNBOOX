# modules/system_info.py

import platform
import socket
import time
import psutil
from datetime import timedelta

def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": psutil.cpu_count(logical=True),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "uptime": str(timedelta(seconds=int(time.time() - psutil.boot_time())))
    }
