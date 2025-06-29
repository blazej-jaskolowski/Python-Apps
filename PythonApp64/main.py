import os
import datetime

# Get input from user
file_path = input("Enter file path: ")

print("\nGetting file timestamps...")

try:
    # Get file stats
    stats = os.stat(file_path)
    
    # Convert timestamps to datetime
    mod_time = datetime.datetime.fromtimestamp(stats.st_mtime)
    access_time = datetime.datetime.fromtimestamp(stats.st_atime)
    
    # On Windows, creation time is available
    if hasattr(stats, 'st_ctime'):
        create_time = datetime.datetime.fromtimestamp(stats.st_ctime)
    else:
        create_time = "Not available"

    print("\nFile timestamps:")
    print(f"Modified time: {mod_time}")
    print(f"Access time: {access_time}")
    print(f"Creation time: {create_time}")
    
except FileNotFoundError:
    print(f"\nError: File '{file_path}' not found")
