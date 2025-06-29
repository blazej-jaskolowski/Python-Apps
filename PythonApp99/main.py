import os
import time
import platform

def clear_screen():
    """Clear the terminal screen using the appropriate command for the OS"""
    print("\nDetecting operating system...")
    system = platform.system().lower()
    
    print(f"Operating System: {platform.system()}")
    
    try:
        if system == 'windows':
            command = 'cls'
            print("Using 'cls' command for Windows")
        else:  # For Linux, macOS, etc.
            command = 'clear'
            print("Using 'clear' command for Unix-based system")
            
        print("\nClearing screen in:")
        # Countdown
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(1)
            
        # Clear screen using OS command
        os.system(command)
        
        print("Screen has been cleared!")
        print(f"Using command: '{command}'")
        print("\nType 'exit' to quit or press Enter to clear screen again")
        
    except Exception as e:
        print(f"\nError clearing screen: {e}")
        print("Try alternative method...")
        
        # Alternative method: print newlines
        print("\n" * 100)
        print("Screen cleared using alternative method (newlines)")

def main():
    print("Screen Clearer Program")
    print("=" * 30)
    print("\nThis program will:")
    print("1. Detect your operating system")
    print("2. Use appropriate command to clear screen")
    print("3. Show a countdown before clearing")
    print("\nPress Enter to continue or type 'exit' to quit")
    
    while True:
        user_input = input("\nCommand: ").lower()
        
        if user_input == 'exit':
            print("\nExiting program...")
            break
        else:
            clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        print("\nThank you for using Screen Clearer!")
 