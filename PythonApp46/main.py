import os
import sys

print("Getting current file information...")

# Get file information
current_file = os.path.abspath(__file__)
file_name = os.path.basename(__file__)
file_path = os.path.dirname(__file__)

print("\nFile Details:")
print(f"Full path: {current_file}")
print(f"File name: {file_name}")
print(f"Directory: {file_path}")

print(f"\nFile statistics:")
stats = os.stat(__file__)
print(f"Size: {stats.st_size} bytes")
print(f"Last modified: {stats.st_mtime}")
