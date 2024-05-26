# Take an array as an input and then insert the next element at any position as the user wants


def custom_in(arr_one, pos, element):
    n = len(arr_one)
    arr_two = [0] * (n + 1)
    for i in range(pos - 1):
        arr_two[i] = arr_one[i]
    arr_two[pos - 1] = element
    for i in range(pos, n + 1):
        arr_two[i] = arr_one[i - 1]
    return arr_two


arr_one = [int(x) for x in input("Enter the elements: ").split(',')]
print(custom_in(arr_one, 2, 10))
