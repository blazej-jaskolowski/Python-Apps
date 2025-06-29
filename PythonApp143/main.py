import platform
import sys
import struct

print("Checking Python bit mode...")

# Method 1: Using platform
print("\nMethod 1: Using platform module")
print(f"Platform architecture: {platform.architecture()}")

# Method 2: Using sys.maxsize
print("\nMethod 2: Using sys.maxsize")
bit_mode = 64 if sys.maxsize > 2**32 else 32
print(f"Bit mode: {bit_mode}-bit")

# Method 3: Using struct
print("\nMethod 3: Using struct module")
struct_bit_mode = struct.calcsize("P") * 8
print(f"Bit mode: {struct_bit_mode}-bit")

print(f"\nFinal result: Python is running in {bit_mode}-bit mode")
