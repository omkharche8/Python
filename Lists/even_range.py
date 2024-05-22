# A program to print even numbers in a range provided
def even_range(start, end):
    x = [i for i in range(start,end+1) if i%2==0]
    return x


start = int(input("Enter start val: "))
end = int(input("Enter end val: "))
print(even_range(start,end))
