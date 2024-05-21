# A python program to find the second-largest number in the list
def second_largest(list1):

    newlist = list(set(sorted(list1)))
    return newlist[-2]


list1 = eval(input("Enter values: "))
print(second_largest(list1))
