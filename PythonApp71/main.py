import os
from datetime import datetime

# Get input from user
directory = input("Enter directory path (press Enter for current directory): ")
directory = directory or "."

print("\nGetting directory listing sorted by creation date...")

# Get list of items with their creation times
items_with_dates = []
try:
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        creation_time = os.path.getctime(item_path)
        items_with_dates.append((creation_time, item_path))

    # Sort items by creation time
    sorted_items = sorted(items_with_dates)

    print("\nDirectory contents sorted by creation date:")
    for timestamp, item_path in sorted_items:
        item_type = "Directory" if os.path.isdir(item_path) else "File"
        size = os.path.getsize(item_path)
        print(f"{datetime.fromtimestamp(timestamp)}: {os.path.basename(item_path)} ({item_type}, {size} bytes)")

    print(f"\nTotal items: {len(sorted_items)}")

except Exception as e:
    print(f"Error accessing directory: {e}")
