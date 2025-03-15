# test_fibonacci_generator_method.py

# Import the function to test
from ..fibonacci_generator_method import fibonacci_generator

# Test 1: First Fibonacci number
assert fibonacci_generator(1) == 1, "Test 1 failed: fibonacci_generator(1) should return 1"

# Test 2: Second Fibonacci number
assert fibonacci_generator(2) == 1, "Test 2 failed: fibonacci_generator(2) should return 1"

# Test 3: Third Fibonacci number
assert fibonacci_generator(3) == 2, "Test 3 failed: fibonacci_generator(3) should return 2"

# Test 4: Tenth Fibonacci number
assert fibonacci_generator(10) == 55, "Test 4 failed: fibonacci_generator(10) should return 55"

# Test 5: Invalid input (n <= 0)
try:
    fibonacci_generator(0)
    assert False, "Test 5 failed: fibonacci_generator(0) should raise ValueError"
except ValueError:
    pass  # Expected behavior

# Test 6: Invalid input (negative number)
try:
    fibonacci_generator(-5)
    assert False, "Test 6 failed: fibonacci_generator(-5) should raise ValueError"
except ValueError:
    pass  # Expected behavior

print("All generator tests passed successfully!")