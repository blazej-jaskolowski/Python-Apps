import platform
import os

# Show calculations
print("Gathering system information...")

# Get system information
os_name = os.name
platform_system = platform.system()
platform_release = platform.release()
platform_version = platform.version()

print(f"\nSystem Details:")
print(f"OS Name: {os_name}")
print(f"Platform: {platform_system}")
print(f"Release: {platform_release}")
print(f"Version: {platform_version}")

print(f"\nFinal result: Running {platform_system} {platform_release}")
