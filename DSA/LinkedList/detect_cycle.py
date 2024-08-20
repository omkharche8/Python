# To determine if a linked list has a cycle, a common approach is to use the Floyd’s Tortoise and Hare algorithm.
# This algorithm uses two pointers, a slow pointer (the tortoise) and a fast pointer (the hare).
# The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
# If there's a cycle in the list, the fast pointer will eventually meet the slow pointer; otherwise, the fast pointer will reach the end of the list (null).


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
