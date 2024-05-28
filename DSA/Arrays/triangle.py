# Checking triangles in an array
# {1,2,3} is a triangle

def check_triangle(arr, n):
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] > arr[k] and arr[j] + arr[k] > arr[i] + arr[k] > arr[j]:
                    count = count + 1

    return count


arr = [10, 21, 22, 100, 101, 200, 300]
n = len(arr)
print(check_triangle(arr, n))
