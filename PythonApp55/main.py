import socket

print("Finding local IP addresses...")

# Get hostname first
hostname = socket.gethostname()
print(f"\nHostname: {hostname}")

# Get local IP
print("\nMethod 1: Using socket.gethostbyname()")
try:
    local_ip = socket.gethostbyname(hostname)
    print(f"Local IP: {local_ip}")
except Exception as e:
    print(f"Error: {e}")

# Get all local IPs
print("\nMethod 2: Getting all local IPs")
try:
    ip_list = socket.gethostbyname_ex(hostname)[2]
    print("All Local IPs:")
    for ip in ip_list:
        print(f"- {ip}")
except Exception as e:
    print(f"Error: {e}")
