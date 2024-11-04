
import os
import time
import psutil
import json

KERNEL_PARAMS = [
    "/proc/sys/vm/swappiness",
    "/proc/sys/vm/dirty_ratio",
    "/proc/sys/kernel/sched_latency_ns"
]

def get_kernel_params():
    params = {}
    for param in KERNEL_PARAMS:
        try:
            with open(param, "r") as file:
                params[param] = file.read().strip()
        except Exception as e:
            print(f"Error reading {param}: {e}")
    return params

def get_system_metrics():
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_io": psutil.disk_io_counters()._asdict(),
        "net_io": psutil.net_io_counters()._asdict()
    }
    return metrics

def collect_data(interval=5, output_file="system_data.json"):
    data = []
    try:
        while True:
            kernel_params = get_kernel_params()
            system_metrics = get_system_metrics()
            timestamp = time.time()
            data_entry = {
                "timestamp": timestamp,
                "kernel_params": kernel_params,
                "system_metrics": system_metrics
            }
            data.append(data_entry)
            print(f"Data collected at {timestamp}: {data_entry}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Data collection stopped.")
    finally:
        with open(output_file, "w") as f:
            json.dump(data, f)
        print(f"Data saved to {output_file}")

if __name__ == "__main__":
    collect_data()
