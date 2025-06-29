import sys

print("Checking system endianness...")

# Check endianness
is_little_endian = sys.byteorder == 'little'

print(f"\nSystem byte order: {sys.byteorder}")
print(f"This is a {'little' if is_little_endian else 'big'}-endian system")

# Demonstrate with a number
num = 1234
bytes_rep = num.to_bytes(4, sys.byteorder)
print(f"\nExample using number {num}:")
print(f"Bytes representation: {list(bytes_rep)}")
