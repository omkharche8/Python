# Reversing list in python
list1 = [int(x) for x in input("Enter values :").split(',')]

def reverse(list1):
    return list1[::-1]


print(reverse(list1))