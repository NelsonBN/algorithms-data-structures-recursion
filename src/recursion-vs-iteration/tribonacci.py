def tribonacci_recursive(n: int): # Time complexity: O(3^n), Space complexity: O(n)
    # Base case
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Recursive case
    return tribonacci_recursive(n - 1) + tribonacci_recursive(n - 2) + tribonacci_recursive(n - 3)


def tribonacci_iteration(n: int): # Time complexity: O(n), Space complexity: O(1)
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    a = 0
    b = 1
    c = 1
    d = 0
    for _ in range(n - 2):
        d = a + b + c
        a = b
        b = c
        c = d

    return c


print(f'recursive(5) = {tribonacci_recursive(11)}') # 274
print(f'iteration(5) = {tribonacci_iteration(11)}') # 274
