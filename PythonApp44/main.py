import site
import sys

print("Locating Python site-packages...")
print("\nSite-packages directories:")

# Get site-packages locations
user_site = site.getusersitepackages()
system_sites = site.getsitepackages()

print("\nUser site-packages:")
print(f"- {user_site}")

print("\nSystem site-packages:")
for path in system_sites:
    print(f"- {path}")

print("\nPython path:")
for path in sys.path:
    print(f"- {path}")
