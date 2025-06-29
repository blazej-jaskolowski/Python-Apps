# Get input from user
given_number = float(input("Enter a number: "))

# Calculate difference and show steps
print(f"\nCalculations:")
print(f"Given number = {given_number}")
print(f"Comparing with 17")

if given_number <= 17:
    difference = 17 - given_number
    print(f"Number is less than or equal to 17")
    print(f"Difference = 17 - {given_number} = {difference}")
else:
    difference = (given_number - 17) * 2
    print(f"Number is greater than 17")
    print(f"Difference = ({given_number} - 17) * 2")
    print(f"         = {given_number - 17} * 2")
    print(f"         = {difference}")

print(f"\nFinal result: {difference}")
