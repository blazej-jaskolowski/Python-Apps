# Define color sets
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# Show calculations
print("Calculations:")
print(f"Color List 1: {color_list_1}")
print(f"Color List 2: {color_list_2}")
print("\nFinding colors in List 1 that are not in List 2...")

# Calculate difference
unique_colors = color_list_1 - color_list_2

print(f"\nFinal result: {unique_colors}")
