import os

# Get input from user
file_path = input("Enter file path: ")

print("\nCalculations:")
print(f"Converting '{file_path}' to absolute path...")

# Get absolute path
abs_path = os.path.abspath(file_path)

print("\nPath details:")
print(f"Original path: {file_path}")
print(f"Directory name: {os.path.dirname(abs_path)}")
print(f"File name: {os.path.basename(abs_path)}")

print(f"\nFinal result: {abs_path}")
