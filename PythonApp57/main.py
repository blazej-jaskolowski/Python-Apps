import time

def example_function():
    # Example function to measure
    sum = 0
    for i in range(1000000):
        sum += i
    return sum

print("Measuring execution time...")

# Method 1: Using time.time()
print("\nMethod 1: Using time.time()")
start_time = time.time()
result = example_function()
end_time = time.time()
execution_time = end_time - start_time

print(f"Result: {result}")
print(f"Execution time: {execution_time:.6f} seconds")

# Method 2: Using time.perf_counter()
print("\nMethod 2: Using time.perf_counter()")
start_time = time.perf_counter()
result = example_function()
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Result: {result}")
print(f"Execution time: {execution_time:.6f} seconds")
