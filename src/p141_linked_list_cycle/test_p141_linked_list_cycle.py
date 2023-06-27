from p141_linked_list_cycle import Solution, ListNode

def test_01():
    head = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(-4)
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = second
    result1 = Solution().hasCycleSet(head)
    result2 = Solution().hasCycleFloyds(head)
    assert result1 == True
    assert result2 == True

def test_02():
    head = ListNode(2)
    second = ListNode(1)
    head.next = second
    second.next = head
    result1 = Solution().hasCycleSet(head)
    result2 = Solution().hasCycleFloyds(head)
    assert result1 == True
    assert result2 == True

def test_03():
    head = ListNode(1)
    result1 = Solution().hasCycleSet(head)
    result2 = Solution().hasCycleFloyds(head)
    assert result1 == False        
    assert result2 == False        