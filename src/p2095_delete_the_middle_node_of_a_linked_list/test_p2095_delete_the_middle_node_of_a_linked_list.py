from p2095_delete_the_middle_node_of_a_linked_list import Solution, ListNode

def test_transformation():
    head = [1,2,3,4,5]
    output = [3,4,5]
    linked1 = Solution().from_vec_to_list_it(head)
    linked2 = Solution().from_vec_to_list_rec(head)
    vec1 = Solution().from_list_to_vec(linked1)
    vec2 = Solution().from_list_to_vec(linked2)
    assert vec1 == vec2

def test_case_01():
    head1 = Solution().from_vec_to_list_it([1, 3, 4, 7, 1, 2, 6])
    output = [1, 3, 4, 1, 2, 6]
    result1 = Solution().delete_middle(head1)
    assert Solution().from_list_to_vec(result1) == output

def test_case_02():
    head1 = Solution().from_vec_to_list_it([1, 2, 3, 4])
    output = [1, 2, 4]
    result1 = Solution().delete_middle(head1)
    assert Solution().from_list_to_vec(result1) == output

def test_case_03():
    head1 = Solution().from_vec_to_list_it([2, 1])
    output = [2]
    result1 = Solution().delete_middle(head1)
    assert Solution().from_list_to_vec(result1) == output

def test_case_04():
    head1 = Solution().from_vec_to_list_it([1])
    output = []
    result1 = Solution().delete_middle(head1)
    assert Solution().from_list_to_vec(result1) == output