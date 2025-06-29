import os

print("Accessing environment variables...")

# Get specific common environment variables
print("\nCommon Environment Variables:")
common_vars = ['PATH', 'HOME', 'USER', 'TEMP']
for var in common_vars:
    value = os.environ.get(var, 'Not Set')
    print(f"{var}: {value}")

# Get user input for specific variable
user_var = input("\nEnter environment variable name to check: ")
value = os.environ.get(user_var, 'Not Found')
print(f"\nValue of {user_var}: {value}")

print(f"\nTotal environment variables: {len(os.environ)}")
