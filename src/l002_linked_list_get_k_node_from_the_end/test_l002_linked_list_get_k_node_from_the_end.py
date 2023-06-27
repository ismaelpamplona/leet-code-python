from l002_linked_list_get_k_node_from_the_end import ListNode, Solution

def test_01():
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    result1 = Solution().get_node_from_the_end(head, 2)
    assert result1 == fourth