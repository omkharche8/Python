# Making even positions greater than odd positions in a given array
def even_odd(nums):
    nums.sort()
    new_arr = [0] * len(nums)
    ptr1 = 0
    ptr2 = len(nums) - 1
    for i in range(len(nums)):
        if i % 2 == 0:
            new_arr[i] = nums[ptr2]
            ptr2 -= 1
        else:
            new_arr[i] = nums[ptr1]
            ptr1 += 1
    for i in range(len(nums)):
        print(new_arr[i], end=" ")


nums = [1, 3, 2]
even_odd(nums)
