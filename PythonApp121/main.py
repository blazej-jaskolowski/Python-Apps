# Example variable that exists
x = 10

# Function to check if variable exists
def is_defined(variable_name):
    return variable_name in locals() or variable_name in globals()

# Test some variables
print("Testing if variables are defined:")

# Test x (which exists)
print(f"\nChecking 'x':")
print(f"Is 'x' defined? {is_defined('x')}")
if is_defined('x'):
    print(f"Value of x: {x}")

# Test y (which doesn't exist)
print(f"\nChecking 'y':")
print(f"Is 'y' defined? {is_defined('y')}")
