# A leader in array is the element which is the last element and the one which is larger than all other elements on right
# Input: arr[] = {16, 17, 4, 3, 5, 2},
# Output: 17, 5, 2

# Input: arr[] = {1, 2, 3, 4, 5, 2},
# Output: 5, 2
def leader(arr, n):
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                break
        if j == n-1:
            print(arr[i], end=' ')


arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
leader(arr, n)
