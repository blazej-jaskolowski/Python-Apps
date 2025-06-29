import os

def display_environment():
    print("User Environment Variables")
    print("=" * 30)
    
    # Get all environment variables
    env_vars = dict(os.environ)
    
    # Common important variables to check
    important_vars = [
        'USERNAME', 'USER', 'HOME', 'PATH', 'LANG',
        'SHELL', 'TEMP', 'PWD', 'COMPUTERNAME'
    ]
    
    print("\nImportant Environment Variables:")
    print("-" * 30)
    for var in important_vars:
        value = env_vars.get(var, 'Not Set')
        print(f"{var}: {value}")
    
    print(f"\nTotal environment variables: {len(env_vars)}")
    
    # Ask if user wants to see all variables
    show_all = input("\nShow all environment variables? (yes/no): ").lower()
    
    if show_all == 'yes':
        print("\nAll Environment Variables:")
        print("-" * 30)
        for key, value in sorted(env_vars.items()):
            print(f"{key}: {value}")

if __name__ == "__main__":
    try:
        display_environment()
    except Exception as e:
        print(f"An error occurred: {e}")
