#factorial_loop_method
def factorial_loop(n):
    if n < 0:
        print("Factoriel is not defiend")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial_loop(5))
