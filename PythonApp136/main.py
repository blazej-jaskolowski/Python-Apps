import os

# Get input from user
directory = input("Enter directory path (press Enter for current directory): ")
directory = directory or "."

print("\nListing only files (skipping directories)...")

try:
    # Get all items
    items = os.listdir(directory)
    
    print("\nFiles found:")
    files = [item for item in items 
            if os.path.isfile(os.path.join(directory, item))]
    
    for i, file in enumerate(files, 1):
        size = os.path.getsize(os.path.join(directory, file))
        print(f"{i}. {file} ({size} bytes)")
    
    print(f"\nTotal files: {len(files)}")
except Exception as e:
    print(f"Error: {e}")
