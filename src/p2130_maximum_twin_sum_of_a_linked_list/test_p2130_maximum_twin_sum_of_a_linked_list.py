from p2130_maximum_twin_sum_of_a_linked_list import ListNode, Solution

def test_transformation():
    head = [1,2,3,4,5]
    output = [3,4,5]
    linked1 = Solution().from_vec_to_list_it(head)
    linked2 = Solution().from_vec_to_list_rec(head)
    vec1 = Solution().from_list_to_vec(linked1)
    vec2 = Solution().from_list_to_vec(linked2)
    assert vec1 == vec2

def test_case_01():
    head = Solution().from_vec_to_list_it([5, 4, 2, 1])
    result = Solution().pair_sum(head)
    assert result == 6

def test_case_02():
    head = Solution().from_vec_to_list_it([4, 2, 2, 3])
    result = Solution().pair_sum(head)
    assert result == 7

def test_case_03():
    head = Solution().from_vec_to_list_it([1, 100000])
    result = Solution().pair_sum(head)
    assert result == 100001