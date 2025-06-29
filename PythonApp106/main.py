import os

# Get input from user
path = input("Enter file path: ")

print("\nSplitting path...")
print(f"Original path: {path}")

# Split using os.path
root, ext = os.path.splitext(path)

print("\nComponents:")
print(f"Root path: {root}")
print(f"Extension: {ext}")

# Additional path information
print("\nAdditional path information:")
print(f"Directory: {os.path.dirname(path)}")
print(f"Filename: {os.path.basename(path)}")
print(f"Absolute path: {os.path.abspath(path)}")
