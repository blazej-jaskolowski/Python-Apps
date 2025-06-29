# Get input from user
kilopascals = float(input("Enter pressure in kilopascals: "))

print("\nCalculations:")
print(f"Converting {kilopascals} kilopascals to other units")

# Conversion factors
psi = kilopascals * 0.145038
mmhg = kilopascals * 7.50062
atm = kilopascals * 0.00986923

print("\nStep by step conversion:")
print(f"To PSI: {kilopascals} * 0.145038 = {psi:.4f}")
print(f"To mmHg: {kilopascals} * 7.50062 = {mmhg:.4f}")
print(f"To atm: {kilopascals} * 0.00986923 = {atm:.4f}")

print("\nFinal results:")
print(f"{kilopascals} kilopascals is equal to:")
print(f"- {psi:.4f} psi")
print(f"- {mmhg:.4f} mmHg")
print(f"- {atm:.4f} atm")
