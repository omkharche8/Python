# Input: arr[] = {1, 0, 0, 1, 0, 1, 1}
# Output: 8
# Explanation: The index range for the 8 sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), (4, 5)(2, 5), (0, 5), (1, 6)

def count_subarray(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += -1 if (arr[j] == 0) else 1
            if sum == 0:
                count += 1

    return count

arr = [1, 0, 0, 1, 0, 1, 1]
print(count_subarray(arr))  # Output: 8
