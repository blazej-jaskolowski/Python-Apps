import os

# Get input from user
path = input("Enter path: ")

print("\nChecking path type...")
print(f"Path: {path}")

if os.path.exists(path):
    print("\nPath exists!")
    if os.path.isfile(path):
        print("This is a file")
        print(f"Size: {os.path.getsize(path)} bytes")
    elif os.path.isdir(path):
        print("This is a directory")
        contents = os.listdir(path)
        print(f"Contains {len(contents)} items")
    elif os.path.islink(path):
        print("This is a symbolic link")
    else:
        print("This is a special file type")
else:
    print("\nPath does not exist")
