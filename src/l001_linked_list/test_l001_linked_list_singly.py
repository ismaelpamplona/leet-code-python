from l001_linked_list import Node

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
one.next = two
two.next = three
three.next = five
head = one

def test_get_sum_singly():
    print("\n")
    # print(head)
    assert head.get_sum() == 11

def test_get_sum_rec_singly():
    assert head.get_sum_rec() == 11

def test_add_node_singly():
    head.add_node(head.next.next, four)
    # print(head)

def test_delete_node_singly():
    head.delete_node(three)
    # print(head)

