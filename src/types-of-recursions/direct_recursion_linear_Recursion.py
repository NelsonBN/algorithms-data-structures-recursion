def countdown(n):
    # Base case
    if n < 0:
        return

    # Recursive case
    print(n)
    countdown(n - 1)

countdown(5)
