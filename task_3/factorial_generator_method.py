#factorial_generator_method

def factorial_generator(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        yield 1
        return
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

def get_factorial(n):
    return list(factorial_generator(n))[-1]

print(get_factorial(5))  # 120