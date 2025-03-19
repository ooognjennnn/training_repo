def fibonacci_generator(n: int):
    """Generates the first n Fibonacci numbers."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    a, b = 1, 1
    for _ in range(n):  # Generate n Fibonacci numbers
        yield a
        a, b = b, a + b