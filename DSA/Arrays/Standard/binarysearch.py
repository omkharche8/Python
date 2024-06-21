# Binary Search standard with Time complexity O(logN)


def binarysearch(arr, key, low, high):
    while low <= high:

        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
    return -1


arr = [2, 3, 4, 10, 40]
key = 10
print(binarysearch(arr, key, 0, len(arr)))
