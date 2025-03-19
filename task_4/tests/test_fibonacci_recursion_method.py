# Absolute import of the Fibonacci recursion method
from task_4.fibonacci_recursion_method import fibonacci_recursion

def test_fibonacci_recursion():
    """Tests for the fibonacci_recursion function."""
    # Test 1: First Fibonacci number
    result = fibonacci_recursion(1)
    assert result == 1, f"Test 1 failed: fibonacci_recursion(1) should return 1, got {result} instead"

    # Test 2: Second Fibonacci number
    result = fibonacci_recursion(2)
    assert result == 1, f"Test 2 failed: fibonacci_recursion(2) should return 1, got {result} instead"

    # Test 3: Third Fibonacci number
    result = fibonacci_recursion(3)
    assert result == 2, f"Test 3 failed: fibonacci_recursion(3) should return 2, got {result} instead"

    # Test 4: Tenth Fibonacci number
    result = fibonacci_recursion(10)
    assert result == 55, f"Test 4 failed: fibonacci_recursion(10) should return 55, got {result} instead"

    # Test 5: Invalid input (n = 0)
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