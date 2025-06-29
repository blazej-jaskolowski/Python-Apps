import os
from pathlib import Path

print("Listing home directory...")

# Get home directory
home = str(Path.home())
print(f"\nHome directory: {home}")

# List contents without absolute path
contents = os.listdir(home)

print("\nContents (relative paths):")
for item in contents:
    item_type = "Directory" if os.path.isdir(os.path.join(home, item)) else "File"
    print(f"{item_type}: {item}")

print(f"\nTotal items: {len(contents)}")
