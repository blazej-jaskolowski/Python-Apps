# Get input from user
items = input("Enter items separated by spaces: ").split()

print("\nOriginal list:", items)

if items:
    # Remove first item using different methods
    print("\nMethod 1: Using pop()")
    removed_item = items.pop(0)
    print(f"Removed item: {removed_item}")
    print(f"Updated list: {items}")
    
    print("\nMethod 2: Using del")
    items_copy = items.copy()
    del items_copy[0]
    print(f"Updated list: {items_copy}")
else:
    print("\nList is empty!")
