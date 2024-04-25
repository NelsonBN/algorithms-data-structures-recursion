def ackermann(m, n):
    # Base case
    if m == 0:
        return n + 1

    # Recursive case
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)

    # Recursive case
    return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(2, 3))
