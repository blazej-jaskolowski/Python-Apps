import sys
import pkgutil

print("Available Built-in Modules:")
print("\nLoading module list...")

# Get all built-in modules
built_in_modules = list(module.name for module in pkgutil.iter_modules())
built_in_modules.sort()

print("\nBuilt-in modules:")
for i, module in enumerate(built_in_modules, 1):
    print(f"{i}. {module}")

print(f"\nTotal built-in modules: {len(built_in_modules)}")
