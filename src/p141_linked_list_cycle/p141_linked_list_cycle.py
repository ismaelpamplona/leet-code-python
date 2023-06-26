from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycleSet(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        h = head
        while h:
            if h in node_set:
                return True
            node_set.add(h)
            h = h.next
        return False

    def hasCycleFloyds(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False