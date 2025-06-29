import subprocess

# Get command from user
command = input("Enter system command: ")

print(f"\nExecuting command: {command}")

try:
    # Execute command and capture output
    result = subprocess.run(command, shell=True, 
                          capture_output=True, text=True)
    
    print("\nCommand output:")
    if result.stdout:
        print("STDOUT:")
        print(result.stdout)
    
    if result.stderr:
        print("STDERR:")
        print(result.stderr)
    
    print(f"\nExit code: {result.returncode}")
except Exception as e:
    print(f"\nError executing command: {e}")
