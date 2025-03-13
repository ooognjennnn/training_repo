#factorial_generator_method

def factorial_generator(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
    if n == 0:
        yield 1
        return
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


for value in factorial_generator(5):
    print(value)