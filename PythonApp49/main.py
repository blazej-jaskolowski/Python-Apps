import os

# Get input from user
directory = input("Enter directory path (press Enter for current directory): ")
directory = directory or "."

print(f"\nListing contents of: {os.path.abspath(directory)}")

try:
    # Get directory contents
    contents = os.listdir(directory)
    
    print("\nFiles and Directories:")
    for item in contents:
        full_path = os.path.join(directory, item)
        item_type = "Directory" if os.path.isdir(full_path) else "File"
        size = os.path.getsize(full_path)
        print(f"{item_type}: {item} ({size} bytes)")
        
    print(f"\nTotal items: {len(contents)}")
except Exception as e:
    print(f"Error accessing directory: {e}")
