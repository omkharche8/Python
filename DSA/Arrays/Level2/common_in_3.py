# ar1[] = {1, 5, 10, 20, 40, 80}
# ar2[] = {6, 7, 20, 80, 100}
# ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20, 80

def common(arr1, arr2, arr3):
    return set(arr1) & set(arr2) & set(arr3)


arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(common(arr1,arr2,arr3))

