import os

# Get current file name
current_file = __file__
new_file = "source_code_copy.py"

print(f"Copying source code from: {current_file}")
print(f"To new file: {new_file}")

try:
    # Read current file
    with open(current_file, 'r') as source:
        code = source.read()
        
    # Write to new file
    with open(new_file, 'w') as target:
        target.write(code)
    
    # Verify copy
    print("\nVerification:")
    print(f"Original size: {os.path.getsize(current_file)} bytes")
    print(f"Copy size: {os.path.getsize(new_file)} bytes")
    print("\nCopy successful!")
except Exception as e:
    print(f"\nError during copy: {e}")
