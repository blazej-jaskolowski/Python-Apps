import sys

print("Python Numeric Limits")
print("=" * 30)

print("\nInteger Limits:")
print(f"Maximum integer: {sys.maxsize}")
print(f"Minimum integer: {-sys.maxsize - 1}")

print("\nFloat Limits:")
print(f"Maximum float: {sys.float_info.max}")
print(f"Minimum float: {sys.float_info.min}")
print(f"Float epsilon: {sys.float_info.epsilon}")
