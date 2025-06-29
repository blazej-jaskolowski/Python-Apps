import time

# Start time
start_time = time.time()

print("Program started...")
print("Simulating some work...")

# Simulate work
time.sleep(2)  # Sleep for 2 seconds

# Calculate runtime
current_time = time.time()
runtime = current_time - start_time

print("\nTime measurements:")
print(f"Start time: {time.ctime(start_time)}")
print(f"Current time: {time.ctime(current_time)}")
print(f"Runtime: {runtime:.2f} seconds")
