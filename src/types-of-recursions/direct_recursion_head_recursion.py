def reverse_string(s):
    # Base case
    if len(s) == 0:
        return s

    # Recursive case
    reversed_rest = reverse_string(s[1:])

    return reversed_rest + s[0]

print(reverse_string("hello world"))
