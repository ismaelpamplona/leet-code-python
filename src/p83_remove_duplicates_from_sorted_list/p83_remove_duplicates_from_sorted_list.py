from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head        