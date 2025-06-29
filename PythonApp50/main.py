# Get input from user
text = input("Enter text to print: ")

print("\nPrinting without spaces or newlines:")
print("Original text:", text)

# Remove spaces and print
no_spaces = text.replace(" ", "")
print("Result:", end="")
for char in no_spaces:
    print(char, end="")
print("\n")  # Final newline for clarity
