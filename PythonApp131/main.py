    # Get input from user
text = input("Enter values separated by spaces: ")

print("\nSplitting string into variables...")
print(f"Original string: '{text}'")

# Split into variables
values = text.split()

print("\nSplit values:")
for i, value in enumerate(values):
    print(f"var{i} = '{value}'")

# Demonstrate dynamic variable assignment
locals().update({f'var{i}': value for i, value in enumerate(values)})
print("\nCreated variables:")
for i in range(len(values)):
    print(f"var{i} = {locals()[f'var{i}']}")
