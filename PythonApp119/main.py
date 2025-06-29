# Get input from user
number = float(input("Enter a floating-point number: "))
places = int(input("Enter number of decimal places: "))

print("\nRounding number...")
print(f"Original number: {number}")
print(f"Decimal places: {places}")

# Different rounding methods
rounded1 = round(number, places)
rounded2 = format(number, f".{places}f")
rounded3 = "{:.{}f}".format(number, places)

print("\nDifferent methods:")
print(f"Method 1 (round): {rounded1}")
print(f"Method 2 (format): {rounded2}")
print(f"Method 3 (string format): {rounded3}")
