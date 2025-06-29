import time
from datetime import datetime

print("Current System Time:")

# Using time module
print("\nMethod 1: Using time module")
print(f"Timestamp: {time.time()}")
print(f"Local time: {time.localtime()}")
print(f"Formatted: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Using datetime module
print("\nMethod 2: Using datetime module")
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Date: {now.date()}")
print(f"Time: {now.time()}")
