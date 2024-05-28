# Sort the array in such a way that first element is the largest then smallest, then second largest then second smallest

def alternate(arr, n):
    arr.sort()
    result = [0] * n
    i = 0
    j = n - 1
    for x in range(n):
        if x % 2 == 0:
            result[x] = arr[j]
            j -= 1
        else:
            result[x] = arr[i]
            i += 1
    return result


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
print(alternate(arr, n))
