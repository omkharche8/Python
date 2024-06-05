#Program to find out the Kth Smallest Element
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
# Output: 7
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
# Output: 10
def kth_smallest(nums, n, k):
    nums.sort()
    print(nums[k-1])


nums = [7, 10, 4, 3, 20, 15]
k = 4
n = len(nums)
kth_smallest(nums, n, k)



