def factorial(n, accumulator=1):
    # Base case
    if n == 0:
        return accumulator

    # Recursive case
    return factorial(n - 1, accumulator * n)


print(factorial(5)) # Output: 120
