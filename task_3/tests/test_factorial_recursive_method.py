from task_3.factorial_recursive_method import factorial_recursive

def test_factorial_recursive():
    """Tests for the factorial_recursive function."""
    assert factorial_recursive(0) == 1, "Test failed for 0!"
    assert factorial_recursive(1) == 1, "Test failed for 1!"
    assert factorial_recursive(5) == 120, "Test failed for 5!"

    # Test negative input
    try:
        factorial_recursive(-1)
        assert False, "Test failed: ValueError not raised for negative input"
    except ValueError:
        pass