import subprocess

# Get input from user
command = input("Enter command to execute: ")

print(f"\nExecuting command: {command}")
print("\nOutput:")

try:
    # Execute command and capture output
    result = subprocess.run(command, shell=True, text=True, 
                          capture_output=True)
    
    print("\nStandard Output:")
    print(result.stdout if result.stdout else "(no output)")
    
    print("\nStandard Error:")
    print(result.stderr if result.stderr else "(no errors)")
    
    print(f"\nExit code: {result.returncode}")
except Exception as e:
    print(f"\nError executing command: {e}")
