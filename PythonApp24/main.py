# Get input from user
letter = input("Enter a single letter: ").lower()

# Show calculations
print(f"\nCalculations:")
print(f"Letter: '{letter}'")
print(f"Checking if letter is a vowel...")

# Define vowels and check
vowels = 'aeiouy'
is_vowel = letter in vowels

if is_vowel:
    print(f"'{letter}' is found in vowels: {vowels}")
else:
    print(f"'{letter}' is not found in vowels: {vowels}")

print(f"\nFinal result: '{letter}' is{' ' if is_vowel else ' not '}a vowel")
