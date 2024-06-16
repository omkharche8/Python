# Input:  arr[] = {1, 2, 3, -4, -1, 4}
# Output: arr[] = {-4, 1, -1, 2, 3, 4}


def rearrange_array(arr):
    n = len(arr)
    oglist = []
    for i in range(n):
        if arr[i] <= 0:
            oglist.append(arr[i])
            continue
        if arr[i] >= 0:
            oglist.append(arr[i])
    return oglist



arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
rearranged_arr = rearrange_array(arr)
print(rearranged_arr)
