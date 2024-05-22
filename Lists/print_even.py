# A Program to print even numbers only in a list
def print_even(list1):
    even_list = []
    for i in list1:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


list1 = [int(x) for x in input("Enter the values: ").split(',')]
print(print_even(list1))
