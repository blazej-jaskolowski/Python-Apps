import os
import getpass

print("Getting username information...")

# Try different methods
print("\nMethods used:")

print("Method 1: Using getpass.getuser()")
username1 = getpass.getuser()
print(f"Result: {username1}")

print("\nMethod 2: Using os.getlogin()")
try:
    username2 = os.getlogin()
    print(f"Result: {username2}")
except Exception as e:
    print(f"Error: {e}")

print("\nMethod 3: Using environment variable")
username3 = os.environ.get('USERNAME', os.environ.get('USER', 'Not Found'))
print(f"Result: {username3}")

print(f"\nFinal result: Current username is '{username1}'")
