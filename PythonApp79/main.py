import sys

def show_size(obj, name="Object"):
    size = sys.getsizeof(obj)
    print(f"\nSize of {name}: {size} bytes")
    return size

# Test with different types
print("Calculating sizes of different objects:")

# Test various types
show_size(42, "Integer")
show_size("Hello", "String")
show_size([1, 2, 3], "List")
show_size({'a': 1, 'b': 2}, "Dictionary")
show_size({1, 2, 3}, "Set")
