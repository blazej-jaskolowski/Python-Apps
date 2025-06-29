import cProfile
import pstats
from pstats import SortKey

def example_function():
    # Example function to profile
    sum = 0
    for i in range(1000):
        sum += i
    return sum

print("Running profiler...")

# Run profiler
profiler = cProfile.Profile()
profiler.enable()
example_function()
profiler.disable()

# Print statistics
print("\nProfiling Statistics:")
stats = pstats.Stats(profiler)
stats.sort_stats(SortKey.TIME)
stats.print_stats()
