def has_odd_product_pair(numbers):
    print("\nChecking for pairs with odd product...")
    
    # Check all distinct pairs
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            product = numbers[i] * numbers[j]
            print(f"Checking {numbers[i]} * {numbers[j]} = {product}")
            if product % 2 == 1:
                print(f"Found odd product: {numbers[i]} * {numbers[j]} = {product}")
                return True
    
    return False

# Get input from user
numbers = input("Enter integers separated by spaces: ").split()
numbers = [int(x) for x in numbers]

print(f"\nNumbers: {numbers}")
result = has_odd_product_pair(numbers)
print(f"\nFinal result: {result}")
