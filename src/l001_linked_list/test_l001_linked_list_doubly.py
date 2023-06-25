from l001_linked_list import DoublyNode

one = DoublyNode(1)
two = DoublyNode(2)
three = DoublyNode(3)
four = DoublyNode(4)
five = DoublyNode(5)
one.next = two
two.prev = one
two.next = three
three.prev = two
three.next = five
five.prev = three
head = one

def test_add_node_doubly():
    print(head)
    head.add_node(five, four)
    print(head)

def test_delete_node_doubly():
    head.delete_node(five)
    print(head)    

