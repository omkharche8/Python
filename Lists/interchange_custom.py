pos1, pos2 = [int(x) for x in input("Enter two index to swap :").split(', ')]


def interchange(list1):
    list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
    return list1


list1 = [3, 4, 5, 6, 8, 9, 10]
print(interchange(list1))
