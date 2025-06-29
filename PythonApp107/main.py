import os
import time

# Get input from user
file_path = input("Enter file path: ")

print("\nRetrieving file properties...")

try:
    # Get file stats
    stats = os.stat(file_path)
    
    print("\nFile Properties:")
    print(f"Size: {stats.st_size} bytes")
    print(f"Mode: {stats.st_mode}")
    print(f"Created: {time.ctime(stats.st_ctime)}")
    print(f"Last modified: {time.ctime(stats.st_mtime)}")
    print(f"Last accessed: {time.ctime(stats.st_atime)}")
    
    # Additional properties
    print("\nPermissions:")
    print(f"Is readable: {os.access(file_path, os.R_OK)}")
    print(f"Is writable: {os.access(file_path, os.W_OK)}")
    print(f"Is executable: {os.access(file_path, os.X_OK)}")
except FileNotFoundError:
    print(f"\nError: File '{file_path}' not found")
