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
    def reverse_between_it(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy: Optional[ListNode] = ListNode(-1, head)
        before: Optional[ListNode] = dummy
        for i in range(1, left):
            before = before.next
        prev = before
        if before:
            cur = before.next
        for i in range(left, right + 1):
            if cur:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
        if before and before.next:
            before.next.next = cur
            before.next = prev
                    
        return dummy.next

    def reverse_between_rec(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(before: Optional[head], left: int, right: int):
            if right == left:
                return before.next

            if before:
                first = before.next
            else:
                before = None

            if right - left > 1:
                rev_sublist_end = reverse(first, left + 1, right - 1)
                rev_sublist_start = first.next
                last = rev_sublist_end.next
            else:
                last = first.next
                rev_sublist_start = first
                rev_sublist_end = last

            after = last.next
            before.next = last
            last.next = rev_sublist_start
            rev_sublist_end.next = first
            first.next = after
            return first

        dummy: Optional[ListNode] = ListNode(-1, head)
        before: Optional[ListNode] = dummy
        for i in range(1, left):
            before = before.next

        reverse(before, left, right)

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
        if n == len(vec):
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

    