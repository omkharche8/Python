# Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
# Output: 5
# Explanation: 5 is the first element that repeats
#
# Input: arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
# Output: 6
# Explanation: 6 is the first element that repeats

def firstRepeat(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return arr[i]


arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
print(firstRepeat(arr))