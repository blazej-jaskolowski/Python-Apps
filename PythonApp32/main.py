# Get input from user
num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

# Show calculations
print(f"\nCalculations:")
print(f"Finding LCM of {num1} and {num2}")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Calculate LCM using formula: LCM = (a * b) / GCD(a,b)
gcd_result = gcd(num1, num2)
lcm_result = (num1 * num2) // gcd_result

print(f"GCD = {gcd_result}")
print(f"LCM = ({num1} * {num2}) / {gcd_result}")

print(f"\nFinal result: LCM = {lcm_result}")
