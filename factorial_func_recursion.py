#factorial_func

def factorial(n):
    if n < 0:
        return "Factorial is not defind for negative numbers"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

        
