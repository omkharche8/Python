# Implementing Counting sort bruv normally

def counting_sort(arr):
    # Find the maximum element in the array
    max_val = max(arr)

    # Initialize the count array with zeros
    count = [0] * (max_val + 1)

    # Store the count of each element in the count array
    for num in arr:
        count[num] += 1

    # Modify the count array to store the cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Initialize the output array
    output = [0] * len(arr)

    # Build the output array using the count array
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
