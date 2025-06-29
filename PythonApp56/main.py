import os
import shutil

print("Getting console window dimensions...")

# Try different methods
print("\nMethods used:")

print("Method 1: Using os.get_terminal_size()")
try:
    terminal_size = os.get_terminal_size()
    print(f"Columns (width): {terminal_size.columns}")
    print(f"Rows (height): {terminal_size.lines}")
except Exception as e:
    print(f"Error with Method 1: {e}")

print("\nMethod 2: Using shutil.get_terminal_size()")
try:
    size = shutil.get_terminal_size()
    print(f"Columns (width): {size.columns}")
    print(f"Rows (height): {size.lines}")
except Exception as e:
    print(f"Error with Method 2: {e}")
