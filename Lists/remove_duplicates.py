# A program to remove duplicates from a list
list1 = [int(x) for x in input("Enter the values : ").split(',')]
print(list(set(list1)))