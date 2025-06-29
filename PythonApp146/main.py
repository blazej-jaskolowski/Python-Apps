import sys
import os

print("Finding Python module sources...")

# Show Python path
print("\nPython path:")
for path in sys.path:
    if os.path.exists(path):
        print(f"\nDirectory: {path}")
        try:
            # List .py files
            py_files = [f for f in os.listdir(path) 
                       if f.endswith('.py')]
            if py_files:
                print("Python files:")
                for file in py_files[:5]:  # Show first 5 files
                    print(f"- {file}")
                if len(py_files) > 5:
                    print(f"... and {len(py_files)-5} more files")
        except Exception as e:
            print(f"Error reading directory: {e}")

print("\nNote: These are the directories Python searches for modules")
