# test_fibonacci_loop_method.py

# Import the function to test
from ..fibonacci_loop_method import fibonacci_loop

# Test 1: First Fibonacci number
assert fibonacci_loop(1) == 1, "Test 1 failed: fibonacci_loop(1) should return 1"

# Test 2: Second Fibonacci number
assert fibonacci_loop(2) == 1, "Test 2 failed: fibonacci_loop(2) should return 1"

# Test 3: Third Fibonacci number
assert fibonacci_loop(3) == 2, "Test 3 failed: fibonacci_loop(3) should return 2"

# Test 4: Tenth Fibonacci number
assert fibonacci_loop(10) == 55, "Test 4 failed: fibonacci_loop(10) should return 55"

# Test 5: Invalid input (n <= 0)
try:
    fibonacci_loop(0)
    assert False, "Test 5 failed: fibonacci_loop(0) should raise ValueError"
except ValueError:
    pass  # Expected behavior

# Test 6: Invalid input (negative number)
try:
    fibonacci_loop(-5)
    assert False, "Test 6 failed: fibonacci_loop(-5) should raise ValueError"
except ValueError:
    pass  # Expected behavior

print("All loop tests passed successfully!")