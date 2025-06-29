import os
from datetime import datetime

# Get input from user
directory = input("Enter directory path (press Enter for current directory): ")
directory = directory or "."

print("\nGetting files and their timestamps...")

# Get list of files with their modification times
files_with_dates = []
try:
    # List all files in directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):  # Check if it's a file (not a directory)
            timestamp = os.path.getmtime(file_path)
            files_with_dates.append((timestamp, file_path))

    # Sort files by timestamp
    sorted_files = sorted(files_with_dates)

    print("\nFiles sorted by date:")
    for timestamp, file_path in sorted_files:
        print(f"{os.path.basename(file_path)}: {datetime.fromtimestamp(timestamp)}")

    print(f"\nTotal files sorted: {len(sorted_files)}")

except Exception as e:
    print(f"Error accessing directory: {e}")