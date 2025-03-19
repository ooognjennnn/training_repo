# Absolute import of the Fibonacci loop method
from task_4.fibonacci_loop_method import fibonacci_loop

def test_fibonacci_loop():
    """Tests for the fibonacci_loop function."""
    # Test 1: First Fibonacci number
    result = fibonacci_loop(1)
    assert result == 1, f"Test 1 failed: fibonacci_loop(1) should return 1, got {result} instead"

    # Test 2: Second Fibonacci number
    result = fibonacci_loop(2)
    assert result == 1, f"Test 2 failed: fibonacci_loop(2) should return 1, got {result} instead"

    # Test 3: Third Fibonacci number
    result = fibonacci_loop(3)
    assert result == 2, f"Test 3 failed: fibonacci_loop(3) should return 2, got {result} instead"

    # Test 4: Tenth Fibonacci number
    result = fibonacci_loop(10)
    assert result == 55, f"Test 4 failed: fibonacci_loop(10) should return 55, got {result} instead"

    # Test 5: Invalid input (n = 0)
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
