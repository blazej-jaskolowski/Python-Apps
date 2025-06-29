# Get input from user
days = int(input("Enter days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

print("\nCalculations:")
print("Converting all units to seconds...")

# Convert each unit to seconds
days_to_sec = days * 24 * 60 * 60
hours_to_sec = hours * 60 * 60
minutes_to_sec = minutes * 60

print(f"\nStep by step:")
print(f"Days to seconds: {days} * 24 * 60 * 60 = {days_to_sec}")
print(f"Hours to seconds: {hours} * 60 * 60 = {hours_to_sec}")
print(f"Minutes to seconds: {minutes} * 60 = {minutes_to_sec}")
print(f"Seconds: {seconds}")

# Calculate total
total_seconds = days_to_sec + hours_to_sec + minutes_to_sec + seconds

print(f"\nFinal result: {total_seconds} seconds")
