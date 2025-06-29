# Get input from user
char = input("Enter a character: ")

print("\nCalculations:")
if len(char) == 1:
    ascii_value = ord(char)
    print(f"ASCII value of '{char}' is {ascii_value}")
    print(f"\nReverse check:")
    print(f"chr({ascii_value}) = '{chr(ascii_value)}'")
else:
    print("Please enter exactly one character")
