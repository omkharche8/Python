#Count pairs with given sum
# Input: arr[] = {1, 5, 7, -1}, K = 6
# Output:  2
# Explanation: Pairs with sum 6 are (1, 5) and (7, -1).
def count_pairs(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                count += 1
    return count


nums = [1, 5, 7, -1]
target = 6
print(count_pairs(nums, target))