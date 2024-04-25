def fibonacci(n):
    # Base case
    if n <= 1:
        return n

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10)) # 55
