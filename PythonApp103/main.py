import os

# Get input from user
path = input("Enter file path: ")

print("\nExtracting filename...")
print(f"Full path: {path}")

# Different methods
print("\nMethod 1: Using os.path.basename()")
filename1 = os.path.basename(path)
print(f"Filename: {filename1}")

print("\nMethod 2: Using string split")
filename2 = path.split(os.sep)[-1]
print(f"Filename: {filename2}")

# Get file parts
name, ext = os.path.splitext(filename1)
print("\nFile components:")
print(f"Name: {name}")
print(f"Extension: {ext}")
