# Counting the occurrences of every number in a list
from collections import Counter
mylist = [int(x) for x in input("Enter the values: ").split(',')]


def count(mylist):
    x = Counter(mylist)
    for element, count in x.items():
        print(f"{element}: {count}")


count(mylist)