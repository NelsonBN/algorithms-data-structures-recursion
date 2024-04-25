def factorial(n): # Time complexity: O(n), Space complexity: O(n)
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


print(f'factorial(3) = {factorial(3)}') # 6
print(f'factorial(4) = {factorial(4)}') # 24
print(f'factorial(5) = {factorial(5)}') # 120
