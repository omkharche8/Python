# Input: arr = {-2,-3,4,-1,-2,1,5,-3}
# Output: 7
# Explanation: The subarray {4,-1, -2, 1, 5} has the largest sum 7.
#
# Input: arr = {2}
# Output: 2
# Explanation: The subarray {2} has the largest sum 2.
#
# Input: arr = {5,4,1,7,8}
# Output: 25
# Explanation: The subarray {5,4,1,7,8} has the largest sum 25.

def largestsum_subarray(arr):
    currSum = 0
    maxSub = arr[0]  #Just something

    for n in arr:
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSub = max(maxSub, currSum)
    return maxSub


arr = [5,4,1,7,8]
print(largestsum_subarray(arr))
