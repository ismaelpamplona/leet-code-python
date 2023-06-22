class ListNode:
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
