class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self, indent=""):
        if self.next is None:
            return f"Node {{\n{indent}  val: {self.val},\n{indent}  next: None\n{indent}}}"
        else:
            next_indent = indent + "    "
            return f"Node {{\n{indent}  val: {self.val},\n{indent}  next: {self.next.__str__(next_indent)}\n{indent}}}"

    def get_sum(self):
        ans = 0
        current = self
        while current:
            ans += current.val
            current = current.next
        return ans

    def get_sum_rec(self):
        if not self:
            return 0
        if not self.next:
            return self.val
        return self.val + self.next.get_sum_rec()

    def add_node(self, prev_node, node_to_add):
        node_to_add.next = prev_node.next
        prev_node.next = node_to_add

    def delete_node(self, prev_node):
        prev_node.next = prev_node.next.next

    def get_middle_node_iterating(self):
        size = 0
        dummy = self

        while dummy:
            size += 1
            dummy = dummy.next

        head = self    
        for i in range(size // 2):
            if head:
                head = head.next

        return head

    def get_middle_node_pointers(self):
        slow = self
        fast = self

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self, indent=""):
        if self.next is None:
            if self.prev is None:
                return f"DoublyNode {{\n{indent}  val: {self.val},\n{indent}  next: None,\n{indent}  prev: None\n{indent}}}"
            else:
                return f"DoublyNode {{\n{indent}  val: {self.val},\n{indent}  next: None,\n{indent}  prev: {self.prev.val}\n{indent}}}"
        else:
            next_indent = indent + "    "
            if self.prev is None:
                return f"DoublyNode {{\n{indent}  val: {self.val},\n{indent}  next: {self.next.__str__(next_indent)},\n{indent}  prev: None\n{indent}}}"
            else:
                return f"DoublyNode {{\n{indent}  val: {self.val},\n{indent}  next: {self.next.__str__(next_indent)},\n{indent}  prev: {self.prev.val}\n{indent}}}"


    def add_node(self, next_node, node_to_add):
        node_to_add.next = next_node
        node_to_add.prev = next_node.prev
        next_node.prev.next = node_to_add
        next_node.prev = node_to_add

    def delete_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

class SentinelNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self, indent=""):
        if self.next is None:
            if self.prev is None:
                return f"SentinelNode {{\n{indent}  val: {self.val},\n{indent}  next: None,\n{indent}  prev: None\n{indent}}}"
            else:
                return f"SentinelNode {{\n{indent}  val: {self.val},\n{indent}  next: None,\n{indent}  prev: {self.prev.val}\n{indent}}}"
        else:
            next_indent = indent + "    "
            if self.prev is None:
                return f"SentinelNode {{\n{indent}  val: {self.val},\n{indent}  next: {self.next.__str__(next_indent)},\n{indent}  prev: None\n{indent}}}"
            else:
                return f"SentinelNode {{\n{indent}  val: {self.val},\n{indent}  next: {self.next.__str__(next_indent)},\n{indent}  prev: {self.prev.val}\n{indent}}}"        

    def add_to_end(self, node_to_add, tail):
        node_to_add.next = tail
        node_to_add.prev = tail.prev
        if tail.prev and tail.prev.next:
            tail.prev.next = node_to_add
        tail.prev = node_to_add

    def delete_from_end(self, head, tail):
        if head.next is not tail:
            if tail.prev.prev:
                tail.prev.prev.next = tail
            if tail.prev:
                tail.prev = tail.prev.prev
    
    def add_to_start(self, node_to_add, head):
        node_to_add.prev = head
        node_to_add.next = head.next
        if head.next:
            head.next.prev = node_to_add
        head.next = node_to_add

    def delete_from_start(self, head, tail):
        if head.next is not tail:
            if head.next.next:
                head.next.next.prev = head
            if head.next:
                head.next = head.next.next




