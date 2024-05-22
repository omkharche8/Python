# A program to print duplicates in a list
list1 = [int(x) for x in input("Enter the values : ").split(',')]
print(list(set([x for x in list1 if list1.count(x) > 1])))