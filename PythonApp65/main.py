# Get input from user
total_seconds = int(input("Enter number of seconds: "))

print("\nCalculations:")
print(f"Converting {total_seconds} seconds to days, hours, minutes, and seconds")

# Calculate each unit
days = total_seconds // (24 * 60 * 60)
remaining = total_seconds % (24 * 60 * 60)
hours = remaining // (60 * 60)
remaining = remaining % (60 * 60)
minutes = remaining // 60
seconds = remaining % 60

print("\nStep by step:")
print(f"Days = {total_seconds} / (24*60*60) = {days}")
print(f"Hours = {remaining} / (60*60) = {hours}")
print(f"Minutes = {remaining} / 60 = {minutes}")
print(f"Seconds = {seconds}")

print(f"\nFinal result: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
