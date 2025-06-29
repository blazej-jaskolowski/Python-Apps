# Get input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Show calculations
print(f"\nCalculations:")
print(f"Numbers: {a}, {b}")
print(f"Checking conditions:")
print(f"1. Are numbers equal? {a} == {b}: {a == b}")
print(f"2. Is sum = 5? {a} + {b} = {a+b}: {a+b == 5}")
print(f"3. Is difference = 5? |{a} - {b}| = {abs(a-b)}: {abs(a-b) == 5}")

result = a == b or a + b == 5 or abs(a - b) == 5

print(f"\nFinal result: {result}")
