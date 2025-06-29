import os
import glob

# Get input from user
pattern = input("Enter search pattern (e.g., *.txt): ")

print(f"\nSearching for files matching: {pattern}")

# Get matching files
files = glob.glob(pattern)

print("\nMatching files:")
for i, file in enumerate(files, 1):
    size = os.path.getsize(file)
    print(f"{i}. {file} ({size} bytes)")

print(f"\nTotal matches found: {len(files)}")
