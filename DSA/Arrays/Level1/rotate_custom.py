# 1 2 3 4 5 is the array
# 4 5 1 2 3 is the output if the input is 2
# This is the super basic method which i know, rotating by one but calling the function multiple times lol
# This is O(n*d)
def custom_rotate(arr, n):
    last_element = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last_element
    return arr


arr = [1, 2, 3, 4, 5]
print(arr)
n = len(arr)
x = 2
for i in range(0, x + 1):
    custom_rotate(arr, n)
print(arr)


# # Optimized way
def custom_rotate(arr, d):
    n = len(arr)
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[(i + d) % n] = arr[i]  # Here im calculating the new position of elements
    return rotated_arr


arr = [1, 2, 3, 4, 5]
d = 2
print("Normal Array: ", arr)
print("Rotated Array: ", custom_rotate(arr, d))


# Using Recursion

def recursive_rotate(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate(arr, d):
    n = len(arr)
    d = d % n
    recursive_rotate(arr, 0, d-1)
    recursive_rotate(arr, d, n-1)
    recursive_rotate(arr, 0, n-1)
    return arr


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
d = 5
print(rotate(arr, d))





