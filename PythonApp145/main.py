def check_type(var):
    print(f"\nAnalyzing variable: {var}")
    print(f"Python type: {type(var)}")
    
    checks = {
        "Is list": isinstance(var, list),
        "Is tuple": isinstance(var, tuple),
        "Is set": isinstance(var, set)
    }
    
    print("\nType checks:")
    for check, result in checks.items():
        print(f"{check}: {result}")
    
    return type(var).__name__

# Test with different types
test_vars = [
    [1, 2, 3],
    (1, 2, 3),
    {1, 2, 3},
    "string",
    42
]

for var in test_vars:
    result = check_type(var)
    print(f"Final result: Variable is a {result}")
