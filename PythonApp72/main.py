import math
import inspect

print("Math Module Details:")
print(f"\nModule Documentation:\n{math.__doc__}")

print("\nModule Constants:")
constants = [attr for attr in dir(math) if not callable(getattr(math, attr))]
for const in constants:
    value = getattr(math, const)
    print(f"{const}: {value}")

print("\nModule Functions:")
functions = [attr for attr in dir(math) if callable(getattr(math, attr))]
for func in functions:
    fn = getattr(math, func)
    if inspect.isbuiltin(fn):
        print(f"\n{func}:")
        print(f"Documentation: {fn.__doc__}")

print(f"\nTotal constants: {len(constants)}")
print(f"Total functions: {len(functions)}")
