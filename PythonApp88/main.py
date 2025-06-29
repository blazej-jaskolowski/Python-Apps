# Define variables
x = 30
y = 20

print("\nCalculations:")
print(f"x = {x}")
print(f"y = {y}")

# Different methods to format
result1 = f"{x}+{y}={x+y}"
result2 = "{}+{}={}".format(x, y, x+y)
result3 = "%d+%d=%d" % (x, y, x+y)

print("\nDifferent formatting methods:")
print(f"Using f-string: {result1}")
print(f"Using format(): {result2}")
print(f"Using % operator: {result3}")
