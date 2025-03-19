# Absolute import for factorial_loop_method
from task_3.factorial_loop_method import factorial_loop

def test_factorial_loop():
    """Tests for the factorial_loop function."""
    assert factorial_loop(0) == 1, "Test failed for 0!"
    assert factorial_loop(1) == 1, "Test failed for 1!"
    assert factorial_loop(5) == 120, "Test failed for 5!"