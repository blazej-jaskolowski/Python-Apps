# Get input from user
num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

# Show calculations
print(f"\nCalculations:")
print(f"Finding GCD of {num1} and {num2}")

def gcd(a, b):
    while b:
        print(f"{a} = {b} * {a//b} + {a%b}")
        a, b = b, a % b
    return a

result = gcd(num1, num2)
print(f"\nFinal result: GCD = {result}")
