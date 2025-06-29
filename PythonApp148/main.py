def find_max_min(numbers):
    if not numbers:
        return None, None
    
    current_max = current_min = numbers[0]
    
    print("\nChecking each number:")
    for num in numbers[1:]:
        if num > current_max:
            print(f"{num} > {current_max} (new maximum)")
            current_max = num
        if num < current_min:
            print(f"{num} < {current_min} (new minimum)")
            current_min = num
        else:
            print(f"Checking {num}...")
    
    return current_max, current_min

# Get input from user
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(x) for x in numbers]

print("\nFinding maximum and minimum...")
print(f"Numbers: {numbers}")

max_num, min_num = find_max_min(numbers)
print(f"\nFinal results:")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")
