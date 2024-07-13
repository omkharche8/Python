def reversebin(n):
    n = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
    reversed_n = n[::-1]  # Reverse the binary string
    return int(reversed_n, 2)  # Convert back to integer from binary

n = 10
print(reversebin(n))
