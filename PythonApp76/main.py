import sys
import argparse

def using_sys_argv():
    print("\nMethod 1: Using sys.argv")
    print("-" * 30)
    
    # Get script name (first argument)
    script_name = sys.argv[0]
    # Get all other arguments
    arguments = sys.argv[1:]
    
    print(f"Script name: {script_name}")
    print(f"Number of arguments: {len(arguments)}")
    
    if arguments:
        print("\nArguments list:")
        for i, arg in enumerate(arguments, 1):
            print(f"Argument {i}: {arg}")
    else:
        print("\nNo arguments provided")

def using_argparse():
    print("\nMethod 2: Using argparse")
    print("-" * 30)
    
    # Create argument parser
    parser = argparse.ArgumentParser(description='Demonstrate command line arguments')
    
    # Add arguments
    parser.add_argument('--name', help='Your name')
    parser.add_argument('--age', type=int, help='Your age')
    parser.add_argument('--show-info', action='store_true', help='Show all information')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Show parsed arguments
    print("\nParsed arguments:")
    for arg in vars(args):
        value = getattr(args, arg)
        if value is not None:
            print(f"{arg}: {value}")

print("Command Line Arguments Demonstration")
print("=" * 40)

# Run both methods
using_sys_argv()
using_argparse()
