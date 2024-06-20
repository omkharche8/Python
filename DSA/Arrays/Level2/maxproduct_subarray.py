# Input: arr[] = {6, -3, -10, 0, 2}
# Output:  180
# Explanation: The subarray is {6, -3, -10}
#
# Input: arr[] = {-1, -3, -10, 0, 60}
# Output:   60
# Explanation: The subarray is {60}

# This is a normal method : O(n^2)

def maxproduct(arr):
    n = len(arr)
    result = arr[0]
    for i in range(n):
        mul = arr[i]
        for j in range(i + 1, n):
            result = max(result, mul)
            mul = mul * arr[j]
        result = max(result, mul)
    return result


arr = [6, -3, -10, 0, 2]
print(maxproduct(arr))


# Using Kadane's Algo

