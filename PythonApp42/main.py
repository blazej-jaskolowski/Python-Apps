import platform

# Show calculations
print("Checking Python architecture...")
print(f"Platform: {platform.platform()}")
print(f"Python version: {platform.python_version()}")

# Get architecture
architecture = platform.architecture()[0]

print(f"\nFinal result: Python is running in {architecture} mode")
