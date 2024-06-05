# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}
#
# Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

def sort012(nums):
    count_0, count_1, count_2 = 0,0,0
    new_arr = []
    for i in nums:
        if i == 0:
            count_0 += 1
        if i == 1:
            count_1 += 1
        if i == 2:
            count_2 += 1
    new_arr = count_0 * [0] + count_1 * [1] + count_2 * [2]
    return  new_arr


nums = [0, 1, 2, 0, 1, 2]
print(sort012(nums))