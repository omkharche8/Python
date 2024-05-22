# A Program to count the number of even and odd numbers in a list

def even_odd(list1):
    even = [x for x in list1 if x % 2 == 0]
    odd = [x for x in list1 if x % 2 != 0]
    return len(even),len(odd)


list1 = [int(x) for x in input("Enter values: ").split(',')]
print(f"Even & Odd : {even_odd(list1)}")