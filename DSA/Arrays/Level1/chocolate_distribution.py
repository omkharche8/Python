# Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that:
#
# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

# Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3
# Output: Minimum Difference is 2
# Explanation:
# We have seven packets of chocolates and we need to pick three packets for 3 students
# If we pick 2, 3 and 4, we get the minimum difference between maximum and minimum packet sizes.


def chocolate(nums,m):
    nums.sort()
    for i in range(m):
        result = nums[-1]-nums[0]
    return result


nums = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(chocolate(nums,m))