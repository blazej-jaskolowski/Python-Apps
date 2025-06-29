import ipaddress

# Get input from user
ip = input("Enter IP address: ")

print("\nValidating IP address...")
print(f"IP address: {ip}")

try:
    # Validate IP address
    ip_obj = ipaddress.ip_address(ip)
    
    print("\nValidation successful!")
    print(f"IP version: IPv{ip_obj.version}")
    print(f"Is private: {ip_obj.is_private}")
    print(f"Is global: {ip_obj.is_global}")
    
except ValueError as e:
    print(f"\nInvalid IP address: {e}")
    print("Example of valid IP: 192.168.1.1")

