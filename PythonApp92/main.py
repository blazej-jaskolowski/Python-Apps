def analyze_string(text):
    print("\nString Analysis:")
    print("-" * 30)
    
    # Show original string
    print(f"Original string: {text}")
    print(f"Length: {len(text)}")
    
    # Show different representations
    print("\nDifferent string representations:")
    print(f"Raw string: {repr(text)}")
    print(f"ASCII encoded: {ascii(text)}")
    print(f"Bytes representation: {text.encode('utf-8')}")
    
    # Analyze special characters
    print("\nCharacter analysis:")
    for i, char in enumerate(text):
        print(f"Position {i}:")
        print(f"  Character: {char}")
        print(f"  ASCII value: {ord(char)}")
        print(f"  Unicode name: {char!r}")
        if ord(char) > 127:  # Non-ASCII character
            print(f"  Unicode escape: \\u{ord(char):04x}")
        print(f"  Is special: {not char.isalnum()}")

def demonstrate_escapes(text):
    print("\nEscape Sequence Examples:")
    print("-" * 30)
    
    # Show with different escape sequences
    print(f"With quotes: \"{text}\"")
    print(f"With single quotes: '{text}'")
    print(f"With newlines:\n{text}")
    print(f"With tabs:\t{text}")
    
    # Create escaped version
    escaped = text.encode('unicode_escape').decode()
    print(f"\nEscaped version: {escaped}")

def main():
    print("Special Characters String Analyzer")
    print("=" * 40)
    print("\nYou can enter any string, including:")
    print("- Special characters (©, ®, ™, etc.)")
    print("- Emojis (😊, 🌟, etc.)")
    print("- Escape sequences (\\n, \\t, etc.)")
    print("- Unicode characters (\\u00A9, etc.)")
    
    # Get input from user
    text = input("\nEnter your string: ")
    
    # Analyze the string
    analyze_string(text)
    
    # Demonstrate escape sequences
    demonstrate_escapes(text)
    
    # Show how to use the string in different contexts
    print("\nUsage Examples:")
    print("-" * 30)
    print(f"1. In a sentence: The text is {text}")
    print(f"2. In uppercase: {text.upper()}")
    print(f"3. In a box:\n+{'-'*len(text)}+\n|{text}|\n+{'-'*len(text)}+")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again with a different string.")
