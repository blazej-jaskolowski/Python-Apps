# Get input from user
text = input("Enter a string: ")

print("\nDisplaying string with double quotes:")

# Different methods
method1 = '"{}"'.format(text)
method2 = f'"{text}"'
method3 = '"' + text + '"'

print("\nDifferent methods:")
print(f"Method 1 (format): {method1}")
print(f"Method 2 (f-string): {method2}")
print(f"Method 3 (concatenation): {method3}")
