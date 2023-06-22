from l001_linked_list import ListNode

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = five
head = one

def test_get_sum():
    print("\n")
    print(head)
    assert head.get_sum() == 11

def test_get_sum_rec():
    assert head.get_sum_rec() == 11

def test_add_node():
    head.add_node(head.next.next, four)
    print(head)

def test_delete_node():
    head.remove_node(three)
    print(head)