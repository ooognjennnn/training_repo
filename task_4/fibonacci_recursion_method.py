def fibonacci_recursion(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)