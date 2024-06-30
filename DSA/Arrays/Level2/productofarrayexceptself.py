# Input: arr[]  = {10, 3, 5, 6, 2}
# Output: prod[]  = {180, 600, 360, 300, 900}


def product(arr):
    n = len(arr)
    new_arr = []
    for i in range(n):
        res = 1
        for j in range(n):
            if i != j:
                res *= arr[j]
        new_arr.append(res)
    return new_arr

arr = [10, 3, 5, 6, 2]
print(product(arr))
