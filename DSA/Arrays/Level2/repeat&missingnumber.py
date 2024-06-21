# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Note that in your output A should precede B.
# Example:
# Input:[3 1 2 5 3]
# Output:[3, 4]
# A = 3, B = 4

def repeat_missing(arr):
    n = len(arr)
    setarr = list(set(arr))

    # Find the duplicate number (A)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                A = arr[i]
                break

    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2

    # Calculate the actual sum of the array
    actual_sum = sum(arr)

    # The missing number (B) can be found as follows:
    B = expected_sum - (actual_sum - A)

    return [A, B]


# Example usage
arr = [3, 1, 2, 5, 3]
print(repeat_missing(arr))  # Output: [3, 4]
