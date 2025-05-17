def factorial_recursive(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    print("n = ", n)
    fac = n * factorial_recursive(n - 1)
    print(fac)
    return fac

print(factorial_recursive(5))
