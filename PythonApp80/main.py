import sys

print("Checking Python recursion limit...")

# Get current limit
current_limit = sys.getrecursionlimit()

print(f"\nCurrent recursion limit: {current_limit}")
print("\nExample of recursive function:")

def recursive_example(n):
    if n <= 0:
        return "Reached base case"
    return recursive_example(n - 1)

print("""def recursive_example(n):
    if n <= 0:
        return "Reached base case"
    return recursive_example(n - 1)""")

print("\nNote: The default limit helps prevent stack overflow")
print("You can change it using sys.setrecursionlimit()")
