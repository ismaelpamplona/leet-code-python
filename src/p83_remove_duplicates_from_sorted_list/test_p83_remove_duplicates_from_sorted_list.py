from p83_remove_duplicates_from_sorted_list import Solution, ListNode

def test_transformation():
    print("PIROCA")
    head = [1,2,3,4,5]
    output = [3,4,5]
    linked1 = Solution().from_vec_to_list_it(head)
    linked2 = Solution().from_vec_to_list_rec(head)
    vec1 = Solution().from_list_to_vec(linked1)
    vec2 = Solution().from_list_to_vec(linked2)
    assert vec1 == vec2

def test_01():
    head = Solution().from_vec_to_list_rec([1,1,2])
    output = [1, 2]
    result = Solution().deleteDuplicates(head)
    assert Solution().from_list_to_vec(result) == output

def test_02():
    head = Solution().from_vec_to_list_rec([1,1,2,3,3])
    output = [1, 2, 3]
    result = Solution().deleteDuplicates(head)
    assert Solution().from_list_to_vec(result) == output