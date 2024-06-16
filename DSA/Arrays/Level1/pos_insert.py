# We will do custom insert here by taking the index as the input

def insert(pos, val, arr):
    n = len(arr)
    arr.append(0)
    for i in range(n, pos, -1):
        arr[i] = arr[i-1]
    arr[pos] = val
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pos = 5
print(insert(pos, 100, arr))
