# Examples:
#
# Input: arr[] = {4, 5, 6, 7, 6}
# k = 1
# x = 6
# Output: 2
# The
# first
# index
# of
# 6 is 2.
#
# Input: arr[] = {20, 40, 50, 70, 70, 60}
# k = 20
# x = 60
# Output: 5
# The
# index
# of
# 60 is 5


def search(k, x, arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] <= k or arr[i] - arr[i-1] >= k:
            if arr[i] == x:
                return i
        else:
            return -1


print(search(20, 60, [20, 40, 50, 70, 70, 60]))
