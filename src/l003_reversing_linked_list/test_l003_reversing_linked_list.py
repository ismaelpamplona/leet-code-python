from l003_reversing_linked_list import Solution, ListNode

def test_01():
    head = Solution().from_vec_to_list_rec([1, 2, 3, 4, 5])
    output = [5, 4, 3, 2, 1]
    reversed_list = Solution().reverse_list(head)
    assert Solution().from_list_to_vec(reversed_list) == output
