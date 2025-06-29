import os

print("Getting process IDs...")

try:
    # Get various IDs
    euid = os.geteuid()
    egid = os.getegid()
    uid = os.getuid()
    gid = os.getgid()
    groups = os.getgroups()
    
    print("\nProcess IDs:")
    print(f"Effective User ID: {euid}")
    print(f"Effective Group ID: {egid}")
    print(f"Real User ID: {uid}")
    print(f"Real Group ID: {gid}")
    print(f"Supplemental Group IDs: {groups}")
except AttributeError:
    print("\nThis functionality is only available on Unix systems")
