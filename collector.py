import platform
import time
import os
import psutil

from datetime import datetime
import pandas as pd

file_path = "data/system_metrics.csv"

while True:
    timestamp = datetime.now()

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    cpu_freq = psutil.cpu_freq().current
    available_ram = psutil.virtual_memory().available / (1024**3)
    free_disk = psutil.disk_usage('/').free / (1024**3)
    machine_name = platform.node()
    cpu_cores = psutil.cpu_count()
    total_ram = psutil.virtual_memory().total / (1024**3)
    data = {
        "timestamp": [timestamp],
        "cpu_usage": [cpu],
        "ram_usage": [ram],
        "disk_usage": [disk],
        "cpu_frequency": [cpu_freq],
        "available_ram_gb": [round(available_ram, 2)],
        "free_disk_gb": [round(free_disk, 2)],
        "machine_name": [machine_name],
        "cpu_cores": [cpu_cores],
        "total_ram_gb": [round(total_ram, 2)]
    }

    df = pd.DataFrame(data)
    print(df)
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

    print("Data saved")
    time.sleep(10)