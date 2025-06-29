# Get input from user
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (%): "))
years = float(input("Enter number of years: "))

# Show calculations
print(f"\nCalculations:")
print(f"Principal amount: ${principal:,.2f}")
print(f"Interest rate: {rate}%")
print(f"Time period: {years} years")
print(f"Formula: Future Value = P(1 + r/100)^t")

# Calculate future value
rate_decimal = rate/100
future_value = principal * (1 + rate_decimal) ** years

print(f"Step by step:")
print(f"= {principal:,.2f} * (1 + {rate_decimal:.3f})^{years}")
print(f"= {principal:,.2f} * {(1 + rate_decimal) ** years:.4f}")

print(f"\nFinal result: ${future_value:,.2f}")
