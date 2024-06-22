# Implementing Stack with a list

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]
# Create a new stack
my_stack = Stack()

# Check if the stack is empty
if my_stack.is_empty():
    print("The stack is empty.")
else:
    print("The stack is not empty.")

my_stack.push(5)
my_stack.push(10)
my_stack.pop()
print(my_stack.peek())
print(my_stack.items)
