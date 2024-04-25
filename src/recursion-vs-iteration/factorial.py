def factorial_recursive(n): # Time complexity: O(n), Space complexity: O(n)
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial_recursive(n - 1)

def factorial_iteration(n): # Time complexity: O(n), Space complexity: O(1)
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(f'(3) recursive = {factorial_recursive(5)}') # 120
print(f'(3) iteration = {factorial_iteration(5)}') # 120
