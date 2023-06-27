import math
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self, indent=""):
        if self.next is None:
            return f"Node {{\n{indent}  val: {self.val},\n{indent}  next: None\n{indent}}}"
        else:
            next_indent = indent + "    "
            return f"Node {{\n{indent}  val: {self.val},\n{indent}  next: {self.next.__str__(next_indent)}\n{indent}}}"

class Solution:
    def from_vec_to_list_it(self, vec: List[int]) -> Optional[ListNode]:
        head = ListNode(vec[0])
        cur = head

        for i in range(1, len(vec)):
            cur.next = ListNode(vec[i])
            cur = cur.next
        
        return head
    
    def from_vec_to_list_rec(self, vec: List[int], n = 0) -> Optional[ListNode]:
        if n == len(vec):
            return None
        head = ListNode(vec[n])
        head.next = Solution().from_vec_to_list_rec(vec, n + 1)
        return head

    def from_list_to_vec(self, head: Optional[ListNode]) -> List[int]:
        vec: List[int] = []
        while head:
            vec.append(head.val)
            head = head.next
        return vec

    def middle_node_floyd(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        return slow

    def middle_node_it(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vec: List[Optional[ListNode]] = []
        cur = head
        while cur is not None:
            vec.append(cur)
            cur = cur.next
        
        mid = math.floor(len(vec)/2)
        return vec[mid]

