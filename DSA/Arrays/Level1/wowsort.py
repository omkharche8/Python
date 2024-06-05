# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

def wowsort(nums):
    new_arr = []
    n = len(nums)
    for i in nums:
        if i <= 0:
            new_arr.append(i)
    for i in nums:
        if i > 0:
            new_arr.append(i)
    return new_arr


nums = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(wowsort(nums))