import psutil

def get_cpu_usage() -> float:
    cpu_usage = psutil.cpu_percent(interval=1.0)
    return cpu_usage

if __name__ == "__main__":
    print(get_cpu_usage())