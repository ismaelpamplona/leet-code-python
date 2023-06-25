from l001_linked_list import SentinelNode

head = SentinelNode(-1)
tail = SentinelNode(-1)
zero = SentinelNode(0)
one = SentinelNode(1)
two = SentinelNode(2)
three = SentinelNode(3)
four = SentinelNode(4)
five = SentinelNode(5)
head.next = one
one.prev = head
one.next = two
two.prev = one
two.next = three
three.prev = two
three.next = four
four.prev = three
four.next = tail
tail.prev = four

def test_add_to_end_sentinel():
    head.add_to_end(five, tail)
    print(head)

def test_delete_from_end_sentinel():
    head.delete_from_end(head, tail)
    print(head)    

def test_add_to_start_sentinel():
    head.add_to_start(zero, head)
    print(head)

def test_delete_from_start_sentinel():
    head.delete_from_start(head, tail)
    print(head)

