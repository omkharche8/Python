# Writing code to reverse an array
def reverse(arr, n):
    i = 0
    j = n - 1
    while i != j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j-1
    return arr


arr = [1, 2, 3, 4, 5]
n = len(arr)
print("Normal array :", arr)
print("Reversed array: ", reverse(arr, n))
