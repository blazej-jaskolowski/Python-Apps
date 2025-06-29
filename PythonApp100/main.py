import socket
import platform

print("Getting host information...")

# Method 1: Using socket
print("\nMethod 1: Using socket")
print(f"Hostname: {socket.gethostname()}")
print(f"FQDN: {socket.getfqdn()}")

# Method 2: Using platform
print("\nMethod 2: Using platform")
print(f"Node: {platform.node()}")
print(f"Platform: {platform.platform()}")
