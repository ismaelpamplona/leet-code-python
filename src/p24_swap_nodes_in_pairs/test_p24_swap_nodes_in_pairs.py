from p24_swap_nodes_in_pairs import Solution, ListNode

def test_transformation():
    head = [1,2,3,4,5]
    output = [3,4,5]
    linked1 = Solution().from_vec_to_list_it(head)
    linked2 = Solution().from_vec_to_list_rec(head)
    vec1 = Solution().from_list_to_vec(linked1)
    vec2 = Solution().from_list_to_vec(linked2)
    assert vec1 == vec2

def test_case_01():
    head1 = Solution().from_vec_to_list_it([1,2,3,4])
    head2 = Solution().from_vec_to_list_it([1,2,3,4])
    output = [2,1,4,3]
    result1 = Solution().swap_pairs_it(head1)
    result2 = Solution().swap_pairs_rec(head2)
    assert Solution().from_list_to_vec(result1) == output
    assert Solution().from_list_to_vec(result2) == output

def test_case_02():
    head1 = Solution().from_vec_to_list_it([])
    head2 = Solution().from_vec_to_list_it([])
    output = []
    result1 = Solution().swap_pairs_it(head1)
    result2 = Solution().swap_pairs_rec(head2)
    assert Solution().from_list_to_vec(result1) == output 
    assert Solution().from_list_to_vec(result2) == output 

def test_case_03():
    head1 = Solution().from_vec_to_list_it([1])
    head2 = Solution().from_vec_to_list_it([1])
    output = [1]
    result1 = Solution().swap_pairs_it(head1)
    result2 = Solution().swap_pairs_rec(head2)
    assert Solution().from_list_to_vec(result1) == output     
    assert Solution().from_list_to_vec(result2) == output     

