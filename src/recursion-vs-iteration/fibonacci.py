def fibonacci_recursive(n): # Time complexity: O(2^n), Space complexity: O(n)
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iteration(n): # Time complexity: O(n), Space complexity: O(1)
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    c = 0
    for _ in range(n - 1):
        c = a + b
        a = b
        b = c

    return b


print(f'recursive(5) = {fibonacci_recursive(13)}') # 233
print(f'iteration(5) = {fibonacci_iteration(13)}') # 233
