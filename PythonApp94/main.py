def display_conversions(byte_string):
    print("\nOriginal byte string:", byte_string)
    print(f"Type: {type(byte_string)}")
    print(f"Length: {len(byte_string)} bytes")

    # Method 1: Using list()
    print("\nMethod 1: Using list()")
    print("-" * 30)
    integers1 = list(byte_string)
    print(f"Result: {integers1}")

    # Method 2: Using list comprehension
    print("\nMethod 2: Using list comprehension")
    print("-" * 30)
    integers2 = [b for b in byte_string]
    print(f"Result: {integers2}")

    # Method 3: Using map
    print("\nMethod 3: Using map()")
    print("-" * 30)
    integers3 = list(map(int, byte_string))
    print(f"Result: {integers3}")

    # Detailed analysis of each byte
    print("\nDetailed byte analysis:")
    print("-" * 30)
    print("Position | Byte | Integer | Binary    | Hex  | ASCII")
    print("-" * 50)
    for i, b in enumerate(byte_string):
        try:
            ascii_char = chr(b) if 32 <= b <= 126 else '.'
        except ValueError:
            ascii_char = '.'
        print(f"{i:8} | {b:4} | {int(b):7} | {bin(b)[2:]:>8} | 0x{b:02x} | {ascii_char}")

def main():
    print("Byte String to Integer List Converter")
    print("=" * 40)
    
    print("\nChoose input method:")
    print("1. Enter a text string (will be converted to bytes)")
    print("2. Enter space-separated byte values (0-255)")
    choice = input("\nEnter choice (1 or 2): ")

    try:
        if choice == '1':
            text = input("\nEnter text string: ")
            byte_string = text.encode('utf-8')
        elif choice == '2':
            values = input("\nEnter byte values (0-255) separated by spaces: ")
            byte_values = [int(x) for x in values.split()]
            # Validate byte values
            for value in byte_values:
                if not 0 <= value <= 255:
                    raise ValueError(f"Invalid byte value: {value}")
            byte_string = bytes(byte_values)
        else:
            raise ValueError("Invalid choice")

        display_conversions(byte_string)

    except ValueError as e:
        print(f"\nError: {e}")
        print("Please ensure all values are between 0 and 255.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
