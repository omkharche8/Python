#Find Sum of Subarrray
# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Output: Sum found between indexes 2 and 4
def subarray_sum(nums, target_sum):
    start = 0
    current_sum = 0
    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum > target_sum:
            current_sum -= nums[start]
            start += 1
        if current_sum == target_sum:
            return start, end
    return None


nums = [1, 4, 20, 3, 10, 5]
n = len(nums)
print(subarray_sum(nums,33))
