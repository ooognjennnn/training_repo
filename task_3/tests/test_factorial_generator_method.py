from ..factorial_generator_method import factorial_generator, get_factorial

def test_factorial_generator():
    # Testiraj generator za n = 5
    gen = factorial_generator(5)
    assert next(gen) == 1, "Test failed for 1!"
    assert next(gen) == 2, "Test failed for 2!"
    assert next(gen) == 6, "Test failed for 3!"
    assert next(gen) == 24, "Test failed for 4!"
    assert next(gen) == 120, "Test failed for 5!"

    # Testing  for  n = 0
    gen = factorial_generator(0)
    assert next(gen) == 1, "Test failed for 0!"

def test_get_factorial():
    # Testing get_factorial for different values.
    assert get_factorial(0) == 1, "Test failed for 0!"
    assert get_factorial(1) == 1, "Test failed for 1!"
    assert get_factorial(5) == 120, "Test failed for 5!"

    # Testing get_factorial for negative input
    try:
        get_factorial(-1)
        assert False, "Test failed: ValueError not raised for negative input"
    except ValueError:
        pass

if __name__ == "__main__":
    test_factorial_generator()
    test_get_factorial()
    print("All factorial_generator tests passed!")