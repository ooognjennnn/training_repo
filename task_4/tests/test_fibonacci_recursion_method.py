# test_fibonacci_recursion_method.py

# Import the function to test
from ..fibonacci_recursion_method import fibonacci_recursion

# Test 1: First Fibonacci number
assert fibonacci_recursion(1) == 1, "Test 1 failed: fibonacci_recursion(1) should return 1"

# Test 2: Second Fibonacci number
assert fibonacci_recursion(2) == 1, "Test 2 failed: fibonacci_recursion(2) should return 1"

# Test 3: Third Fibonacci number
assert fibonacci_recursion(3) == 2, "Test 3 failed: fibonacci_recursion(3) should return 2"

# Test 4: Tenth Fibonacci number
assert fibonacci_recursion(10) == 55, "Test 4 failed: fibonacci_recursion(10) should return 55"

# Test 5: Invalid input (n <= 0)
try:
    fibonacci_recursion(0)
    assert False, "Test 5 failed: fibonacci_recursion(0) should raise ValueError"
except ValueError:
    pass  # Expected behavior

# Test 6: Invalid input (negative number)
try:
    fibonacci_recursion(-5)
    assert False, "Test 6 failed: fibonacci_recursion(-5) should raise ValueError"
except ValueError:
    pass  # Expected behavior

print("All recursion tests passed successfully!")