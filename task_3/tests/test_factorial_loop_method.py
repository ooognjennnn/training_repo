from ..factorial_loop_method import factorial_loop

def test_factorial_loop():
    assert factorial_loop(0) == 1, "Test failed for 0!"
    assert factorial_loop(1) == 1, "Test failed for 1!"
    assert factorial_loop(5) == 120, "Test failed for 5!"

if __name__ == "__main__":
    test_factorial_loop()
    print("All factorial_loop tests passed!")