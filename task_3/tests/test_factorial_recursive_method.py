from ..factorial_recursive_method import factorial_recursive

def test_factorial_recursive():
    assert factorial_recursive(0) == 1, "Test failed for 0!"
    assert factorial_recursive(1) == 1, "Test failed for 1!"
    assert factorial_recursive(5) == 120, "Test failed for 5!"

if __name__ == "__main__":
    test_factorial_recursive()
    print("All factorial_recursive tests passed!")