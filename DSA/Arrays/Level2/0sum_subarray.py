# Input: {4, 2, -3, 1, 6}
# Output: true
# Explanation:
# There is a subarray with zero-sum from index 1 to 3.
#
# Input: {4, 2, 0, 1, 6}
# Output: true
# Explanation: The third element is zero. A single element is also a sub-array.
#
# Input: {-3, 2, 3, 1, 6}
# Output: false


def sum0_subarray(arr):
    n = len(arr)
    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ = summ + arr[j]
            if summ == 0:
                return True
    return False


arr = [4, 2, -3, 1, 6]
print(sum0_subarray(arr))