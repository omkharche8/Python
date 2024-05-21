# A Program to find out the smallest and largest value in a list

def small_large(list1):
    newlist1 = sorted(list1)
    return newlist1[0], newlist1[-1]


list1 = [int(x) for x in input("Enter the values: ").split(',')]
small, large = small_large(list1)
print(f"Smallest value: {small}\nlargest value: {large}")