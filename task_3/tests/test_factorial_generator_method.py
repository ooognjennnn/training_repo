# Absolute import for factorial_generator_method
from task_3.factorial_generator_method import factorial_generator, get_factorial

def test_factorial_generator():
    """Tests for the factorial_generator function."""
    # Test generator for n = 5
    gen = factorial_generator(5)
    assert next(gen) == 1, "Test failed for 1!"
    assert next(gen) == 2, "Test failed for 2!"
    assert next(gen) == 6, "Test failed for 3!"
    assert next(gen) == 24, "Test failed for 4!"
    assert next(gen) == 120, "Test failed for 5!"

    # Test generator for n = 0
    gen = factorial_generator(0)
    assert next(gen) == 1, "Test failed for 0!"

def test_get_factorial():
    """Tests for the get_factorial function."""
    # Test get_factorial for different values
    assert get_factorial(0) == 1, "Test failed for 0!"
    assert get_factorial(1) == 1, "Test failed for 1!"
    assert get_factorial(5) == 120, "Test failed for 5!"

    # Test that get_factorial raises ValueError for negative input
    try:
        get_factorial(-1)
        assert False, "Test failed: ValueError not raised for negative input"
    except ValueError:
        pass