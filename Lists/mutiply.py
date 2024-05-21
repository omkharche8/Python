# Python Program to multiply all numbers in list
def multiply(list1):
    result = 1
    for x in list1:
        result = result * x
    return result


list1 = eval(input("Enter values: "))
print(multiply(list1))