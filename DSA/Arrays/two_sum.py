# In this problem, we need to find the pair of the two elements from the given list whose sum is equal to the given target value. We can assume that the array has only one pair of integers that add up to the target sum.
def twosum(arr, n, key):
    for i in range(n):
        for j in range(i,n):
            if key == arr[i] + arr[j]:
                return i,j

arr = [0,1,2,3,4,5]
n = len(arr)
key = 10
print(twosum(arr,n,key))

