from p876_middle_of_the_linked_list import Solution, ListNode

def test_transformation():
    head = [1,2,3,4,5]
    output = [3,4,5]
    linked1 = Solution().from_vec_to_list_it(head)
    linked2 = Solution().from_vec_to_list_rec(head)
    vec1 = Solution().from_list_to_vec(linked1)
    vec2 = Solution().from_list_to_vec(linked2)
    assert vec1 == vec2

def test_01():
    head = Solution().from_vec_to_list_rec([1, 2, 3, 4, 5])
    output = [3, 4, 5]
    middle1 = Solution().middle_node_floyd(head)
    middle2 = Solution().middle_node_it(head)
    assert Solution().from_list_to_vec(middle1) == output
    assert Solution().from_list_to_vec(middle2) == output

def test_02():
    head = Solution().from_vec_to_list_rec([1, 2, 3, 4, 5, 6])
    output = [4, 5, 6]
    middle1 = Solution().middle_node_floyd(head)
    middle2 = Solution().middle_node_it(head)
    assert Solution().from_list_to_vec(middle1) == output
    assert Solution().from_list_to_vec(middle2) == output
