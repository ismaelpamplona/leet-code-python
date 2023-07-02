from p92_reverse_linked_list_ii import Solution, ListNode

def test_transformation():
    head = [1,2,3,4,5]
    output = [3,4,5]
    linked1 = Solution().from_vec_to_list_it(head)
    linked2 = Solution().from_vec_to_list_rec(head)
    vec1 = Solution().from_list_to_vec(linked1)
    vec2 = Solution().from_list_to_vec(linked2)
    assert vec1 == vec2

def test_01():
    head1 = Solution().from_vec_to_list_rec([1, 2, 3, 4, 5])
    output = [1, 4, 3, 2, 5]
    reversed1 = Solution().reverse_between_it(head1, 2, 4)
    assert Solution().from_list_to_vec(reversed1) == output

def test_02():
    head1 = Solution().from_vec_to_list_rec([5])
    output = [5]
    reversed1 = Solution().reverse_between_it(head1, 1, 1)
    assert Solution().from_list_to_vec(reversed1) == output

def test_03():
    head1 = Solution().from_vec_to_list_rec([1, 2, 3, 4, 5, 6, 7])
    output = [1, 2, 5, 4, 3, 6, 7]
    reversed1 = Solution().reverse_between_it(head1, 3, 5)
    assert Solution().from_list_to_vec(reversed1) == output
