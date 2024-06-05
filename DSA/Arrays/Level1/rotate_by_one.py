# What we will do here is,
# 1 2 3 4 as
# 3 4 1 2  as the output


def rotate(arr, d):
    last_element = arr[d - 1]
    for x in range(d - 1, 0, -1):
        arr[x] = arr[x - 1]

    arr[0] = last_element


arr = [1, 2, 3, 4, 5]
d = len(arr)
print("Normal Array: ", arr)
rotate(arr,d)
for i in range(0, d):
    print(arr[i], end=" ")

