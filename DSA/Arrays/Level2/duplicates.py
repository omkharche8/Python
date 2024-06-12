# Find duplicates in the array
# Input: n=7 , array[]={1, 2, 3, 6, 3, 6, 1}
# Output: 1, 3, 6
# Explanation: The numbers 1 , 3 and 6 appears more than once in the array.


def duplicate(nums):
    num_set = set()
    dups = set()

    for num in nums:
        if num in num_set:
            dups.add(num)
        else:
            num_set.add(num)
    return list(dups)


nums = [1, 2, 3, 6, 3, 6, 1]
print(duplicate(nums))
