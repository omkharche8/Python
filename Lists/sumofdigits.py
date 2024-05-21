# Sum of Digits of elements in the list
def sum_of_digits(list1):
    result = []
    for ele in list1:
        sum = 0
        for digit in str(ele):
            sum += int(digit)
        result.append(sum)
    return result


# list1 = [int(x) for x in input("Enter values :").split(',')]
list1 = eval(input("Enter values: :"))
print(sum_of_digits(list1))