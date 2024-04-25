def binary_search_recursive(arr, target, low, high): # Time complexity: O(log(n)), Space complexity: O(log(n))
    # Base case - If the low index is greater than the high index, the target is not in the array
    if low > high:
        return -1

    mid = high - (high - low) // 2
    # Base case - If the middle element is the target, return the index of the middle element
    if arr[mid] == target:
        return mid

    # Recursive case - If the middle element is greater than the target, search the left half of the array
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)

    # Recursive case - If the middle element is less than the target, search the right half of the array
    return binary_search_recursive(arr, target, mid + 1, high)


def binary_search_iteration(arr, target): # Time complexity: O(log(n)), Space complexity: O(1)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = high - (high - low) // 2
        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1


arr = [12, 23, 34, 45, 56, 67, 78, 89, 90]

print(f'recursive(arr, 5, 0, len(arr) - 1) = {binary_search_recursive(arr, 45, 0, len(arr) - 1)}') # 4
print(f'iteration(arr, 5) = {binary_search_iteration(arr, 45)}') # 4
