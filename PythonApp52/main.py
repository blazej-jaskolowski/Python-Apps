import sys

# Get input from user
message = input("Enter message to print to stderr: ")

print("\nPrinting to different streams:")
print("This goes to stdout (standard output)")
print(f"Error: {message}", file=sys.stderr)

# Show where output went
print("\nOutput streams used:")
print(f"stdout: {sys.stdout.name}")
print(f"stderr: {sys.stderr.name}")
