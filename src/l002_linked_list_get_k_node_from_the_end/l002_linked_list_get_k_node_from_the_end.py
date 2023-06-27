from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_node_from_the_end(self, head: Optional[ListNode], k) -> bool:
        slow = head
        fast = head
        for _ in range(k):
            fast = fast.next
        while slow and fast:
            slow = slow.next
            fast = fast.next
        return slow