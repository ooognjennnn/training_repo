# Absolute import of the Fibonacci generator function
from task_4.fibonacci_generator_method import fibonacci_generator

def test_fibonacci_generator():
    """Tests for the fibonacci_generator function."""
    # Test 1: First Fibonacci number
    result = list(fibonacci_generator(1))
    assert result == [1], f"Test 1 failed: fibonacci_generator(1) should return [1], got {result} instead"

    # Test 2: First two Fibonacci numbers
    result = list(fibonacci_generator(2))
    assert result == [1, 1], f"Test 2 failed: fibonacci_generator(2) should return [1, 1], got {result} instead"

    # Test 3: First three Fibonacci numbers
    result = list(fibonacci_generator(3))
    assert result == [1, 1, 2], f"Test 3 failed: fibonacci_generator(3) should return [1, 1, 2], got {result} instead"

    # Test 4: First ten Fibonacci numbers
    result = list(fibonacci_generator(10))
    assert result == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55], (
        f"Test 4 failed: fibonacci_generator(10) should return [1, 1, 2, 3, 5, 8, 13, 21, 34, 55], got {result} instead"
    )

    # Test 5: Invalid input (n = 0)
    try:
        list(fibonacci_generator(0))
        assert False, "Test 5 failed: fibonacci_generator(0) should raise ValueError"
    except ValueError:
        pass  # Expected behavior

    # Test 6: Invalid input (negative number)
    try:
        list(fibonacci_generator(-5))
        assert False, "Test 6 failed: fibonacci_generator(-5) should raise ValueError"
    except ValueError:
        pass  # Expected behavior
