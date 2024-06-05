# Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
# Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

# Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
# Output : arr[] = {1, 2, 3, 6, 0, 0, 0};

def move_zeroes(arr):
    new_arr = [x for x in arr if x != 0]
    new_arr += [0] * arr.count(0)
    return new_arr


arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(move_zeroes(arr))
