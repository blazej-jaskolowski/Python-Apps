from collections import Counter

# Get input from user
items = input("Enter items separated by spaces: ").split()

print("\nCounting items...")
print(f"Original items: {items}")

# Create counter
counter = Counter(items)

print("\nItem counts:")
for item, count in counter.items():
    print(f"{item}: {count}")

# Calculate sum of counts
total = sum(counter.values())

print(f"\nFinal result: Total count = {total}")
