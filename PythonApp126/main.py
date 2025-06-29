import inspect

def get_module(obj):
    print(f"\nAnalyzing object: {obj}")
    print(f"Type: {type(obj)}")
    
    # Get module
    module = inspect.getmodule(obj)
    print(f"Module: {module}")
    
    return module

# Test with different objects
print("Testing different objects:")

# Test with built-in objects
print("\nBuilt-in list:")
get_module(list)

print("\nBuilt-in dict:")
get_module(dict)

# Test with custom function
def test_function():
    pass

print("\nCustom function:")
get_module(test_function)
