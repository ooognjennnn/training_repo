#factorial_func

def factorial_recursion(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)
    


print(factorial_recursion(-5))

        
