import os

# Get input from user
file_path = input("Enter file path: ")

print("\nGetting file size...")

try:
    # Get size in bytes
    size_bytes = os.path.getsize(file_path)
    
    # Convert to different units
    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    
    print("\nFile size in different units:")
    print(f"Bytes: {size_bytes:,}")
    print(f"Kilobytes: {size_kb:.2f}")
    print(f"Megabytes: {size_mb:.2f}")
except FileNotFoundError:
    print(f"\nError: File '{file_path}' not found")

