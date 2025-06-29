def check_sequences(binary_str):
    print(f"\nAnalyzing sequence: {binary_str}")
    
    # Find all sequences of zeros
    zero_sequences = []
    current_count = 0
    
    for i, char in enumerate(binary_str):
        if char == '0':
            current_count += 1
        elif current_count > 0:
            zero_sequences.append((i - current_count, current_count))
            current_count = 0
    
    if current_count > 0:
        zero_sequences.append((len(binary_str) - current_count, current_count))
    
    print("\nChecking sequences:")
    # Check each sequence of zeros
    for start, length in zero_sequences:
        print(f"Found {length} zeros at position {start}")
        # Check if followed by same number of ones
        if start + length + length > len(binary_str):
            print(f"Not enough characters left for ones sequence")
            return False
        
        ones_sequence = binary_str[start + length:start + length + length]
        if ones_sequence != '1' * length:
            print(f"Expected {length} ones, found: {ones_sequence}")
            return False
        print(f"Followed by {length} ones: OK")
    
    return True

# Test the function
test_sequences = ['01010101', '00', '000111000111', '00011100011']

for sequence in test_sequences:
    result = check_sequences(sequence)
    print(f"\nResult for {sequence}: {result}")
