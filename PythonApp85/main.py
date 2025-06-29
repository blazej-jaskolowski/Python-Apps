import os

# Get input from user
path = input("Enter a file path: ")

print("\nChecking path...")
print(f"Path: {path}")

# Check path
if os.path.exists(path):
    if os.path.isfile(path):
        print(f"\nThis is a file")
        print(f"File size: {os.path.getsize(path)} bytes")
        print(f"Last modified: {os.path.getmtime(path)}")
    elif os.path.isdir(path):
        print(f"\nThis is a directory")
        print(f"Contents: {os.listdir(path)}")
    else:
        print("\nThis is a special file (neither regular file nor directory)")
else:
    print("\nPath does not exist")
