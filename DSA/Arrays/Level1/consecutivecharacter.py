def removeConsecutiveCharacter(self, S):
    mystring = ""
    for i in range(len(S)):
        if i == 0 or S[i] != S[i - 1]:
            mystring += S[i]
    return mystring


