# Implementing 2 stacks but in one array only
# We will be starting one stack from the stack[0] and other from stack[-1]
# This is the total plan


class TwoStacksOneArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nums = [None] * capacity
        self.topa = -1
        self.topb = capacity

    def pusha(self, data):
        if self.topa + 1 == self.topb:
            print("Overflow")
        else:
            self.topa += 1
            self.nums[self.topa] = data

    def pushb(self, data):
        if self.topa + 1 == self.topb:
            print("Overflow")
        else:
            self.topb -= 1
            self.nums[self.topb] = data

    def popa(self):
        if self.topa == -1:
            print("Underflow")
            return None
        else:
            data = self.nums[self.topa]
            self.topa -= 1
            return data

    def popb(self):
        if self.topb == self.capacity:
            print("Underflow")
            return None
        else:
            data = self.nums[self.topb]
            self.topb += 1
            return data

# Example usage:
capacity = 10
stacks = TwoStacksOneArray(capacity)
stacks.pusha(1)
stacks.pusha(2)
stacks.pushb(3)
stacks.pushb(4)
print(stacks.nums)  # Output should show the internal state of the array with elements pushed to both stacks
print(stacks.popa())  # Output: 2
print(stacks.popb())  # Output: 4


