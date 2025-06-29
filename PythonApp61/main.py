# Get input from user
feet = float(input("Enter distance in feet: "))

print("\nCalculations:")
print(f"Converting {feet} feet to other units")

# Conversion factors
inches = feet * 12
yards = feet / 3
miles = feet / 5280

print("\nStep by step conversion:")
print(f"To inches: {feet} * 12 = {inches:.2f} inches")
print(f"To yards: {feet} / 3 = {yards:.2f} yards")
print(f"To miles: {feet} / 5280 = {miles:.4f} miles")

print("\nFinal results:")
print(f"{feet} feet is equal to:")
print(f"- {inches:.2f} inches")
print(f"- {yards:.2f} yards")
print(f"- {miles:.4f} miles")
