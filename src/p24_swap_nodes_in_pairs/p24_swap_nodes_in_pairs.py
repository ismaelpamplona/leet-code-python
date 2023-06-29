from typing import Optional, List

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
    def swap_pairs_it(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:            
            return None
        cur = head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while cur and cur.next:
            first = cur
            second = cur.next

            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            cur = first.next
        return dummy.next

        
    def swap_pairs_rec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = Solution().swap_pairs_rec(second.next)
        second.next = first
        return second

    def from_vec_to_list_rec(self, vec: List[int], n = 0) -> Optional[ListNode]:
        if n == len(vec):
            return None
        head = ListNode(vec[n])
        head.next = Solution().from_vec_to_list_rec(vec, n + 1)
        return head         

    def from_vec_to_list_it(self, vec: List[int]) -> Optional[ListNode]:
        if len(vec) == 0:
            return None
        head = ListNode(vec[0])
        cur = head
        for i in range(1, len(vec)):
            cur.next = ListNode(vec[i])
            cur = cur.next
        return head    

    def from_list_to_vec(self, head: Optional[ListNode]) -> List[int]:
        if head == None:
            return []
        vec: List[int] = []
        cur = head
        while cur:
            vec.append(cur.val)
            cur = cur.next
        return vec
