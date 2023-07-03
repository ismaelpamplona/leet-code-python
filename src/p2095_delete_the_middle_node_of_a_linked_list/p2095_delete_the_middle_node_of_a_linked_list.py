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
    def delete_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dummy = ListNode(-1, head)
        slow = dummy.next
        prev = dummy.next
        fast = dummy.next

        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return dummy.next
        
    def from_vec_to_list_it(self, vec: List[int]) -> Optional[ListNode]:
        if len(vec) == 0:
            return None
        head = ListNode(vec[0])
        cur = head
        for i in range(1, len(vec)):
            cur.next = ListNode(vec[i])
            cur = cur.next
        return head
    
    def from_vec_to_list_rec(self, vec: List[int], n = 0) -> Optional[ListNode]:
        if n >= len(vec):
            return None
        head = ListNode(vec[n])
        head.next = Solution().from_vec_to_list_rec(vec, n + 1)
        return head

    def from_list_to_vec(self, head: Optional[ListNode]) -> List[int]:
        vec: List[int] = []
        cur = head
        while cur:
            vec.append(cur.val)
            cur = cur.next
        return vec