import multiprocessing
import os

print("Gathering CPU information...")

# Show calculations
print("\nCalculations:")
print("Method 1: Using multiprocessing.cpu_count()")
cpu_count_mp = multiprocessing.cpu_count()
print(f"Result: {cpu_count_mp} CPUs")

print("\nMethod 2: Using os.cpu_count()")
cpu_count_os = os.cpu_count()
print(f"Result: {cpu_count_os} CPUs")

# On Linux systems, we can also check /proc/cpuinfo
if os.path.exists('/proc/cpuinfo'):
    print("\nMethod 3: Reading /proc/cpuinfo")
    try:
        with open('/proc/cpuinfo') as f:
            cpu_info = f.readlines()
        physical_cpus = len([line for line in cpu_info if line.startswith('processor')])
        print(f"Result: {physical_cpus} CPUs")
    except Exception as e:
        print(f"Could not read /proc/cpuinfo: {e}")

print(f"\nFinal result: System has {cpu_count_mp} CPU(s)")
