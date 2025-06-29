import traceback

def function3():
    print("\nCurrent call stack:")
    traceback.print_stack()

def function2():
    function3()

def function1():
    function2()

print("Demonstrating call stack...")
function1()
