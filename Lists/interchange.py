# A code to interchange the first and last elements in a list
def interchange(testlist):
    testlist[0], testlist[-1] = testlist[-1], testlist[0]
    return testlist


testlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(interchange(testlist))



