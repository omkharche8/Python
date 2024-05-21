# A program to calculate the sum and avg of values in the list
list1 = [int(x) for x in input("Enter the values :").split(',')]


def avg_sum(list1):
    count = 0
    for i in list1:
        count += i
    avg = count/len(list1)
    return count, avg


print(avg_sum(list1))