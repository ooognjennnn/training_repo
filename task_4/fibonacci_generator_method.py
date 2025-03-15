def fibonacci_generator(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    def fib_gen():
        a, b = 1, 1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b

    fib = fib_gen()
    for _ in range(n):
        result = next(fib)
    return result