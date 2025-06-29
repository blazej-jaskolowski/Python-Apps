# Get input from user
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

print("\nCalculations:")
print("BMI Formula: weight / (height * height)")

# Calculate BMI
bmi = weight / (height ** 2)

print(f"\nStep by step:")
print(f"BMI = {weight} / ({height} * {height})")
print(f"BMI = {weight} / {height**2}")

print(f"\nFinal result: BMI = {bmi:.2f}")

# BMI Categories
print("\nBMI Categories:")
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your category: {category}")
