# Get input from user
numbers = input("Enter numbers (0-255) separated by spaces: ").split()
numbers = [int(x) for x in numbers]

print("\nCreating bytearray...")
print(f"Original numbers: {numbers}")

try:
    # Create bytearray
    byte_array = bytearray(numbers)
    
    print("\nBytearray details:")
    print(f"Bytes: {byte_array}")
    print(f"Length: {len(byte_array)} bytes")
    print("\nIndividual bytes:")
    for i, b in enumerate(byte_array):
        print(f"Byte {i}: {b} (hex: {hex(b)})")
except ValueError as e:
    print(f"\nError: {e}")
    print("All values must be between 0 and 255")
