import os

# Get input from user
filename = input("Enter filename to check: ")

# Show calculations
print(f"\nChecking if file '{filename}' exists...")

# Check file existence
exists = os.path.exists(filename)

if exists:
    print(f"File details:")
    print(f"Size: {os.path.getsize(filename)} bytes")
    print(f"Last modified: {os.path.getmtime(filename)}")

print(f"\nFinal result: File {'exists' if exists else 'does not exist'}")

# Test command: PythonApp34