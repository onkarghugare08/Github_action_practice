import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")

if cpu > 95:
    raise SystemExit("CPU usage is too high")

if memory > 95:
    raise SystemExit("Memory usage is too high")

if disk > 95:
    raise SystemExit("Disk usage is too high")

print("System health check passed!")