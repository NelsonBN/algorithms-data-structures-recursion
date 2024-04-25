def power_recursive(base, exponent): # Time complexity: O(n), Space complexity: O(n)
    # Base case
    if exponent == 0:
        return 1

    # Recursive case
    return base * power_recursive(base, exponent - 1)


def power_iteration(base, exponent): # Time complexity: O(n), Space complexity: O(1)
    result = 1
    for _ in range(exponent):
        result *= base
    return result


print(f'recursive(2, 3) = {power_recursive(2, 3)}') # 8
print(f'iteration(2, 3) = {power_iteration(2, 3)}') # 8
