#Input: array[]= {5, 10, 20, 15}
# Output: 20
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

# Input: array[] = {10, 20, 15, 2, 23, 90, 67}
# Output: 20 or 90
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.

def peak_element(arr,n):
    new_list = []
    for i in range(1,n-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            new_list.append(arr[i])
    return new_list


arr = [10, 20, 15, 2, 23, 90, 67]
n = len(arr)
print(peak_element(arr,n))
