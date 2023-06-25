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
        node.prev.next = node.next
        node.next.prev = node.prev



