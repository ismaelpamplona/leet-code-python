from p1047_remove_all_adjacent_duplicates_in_string import Solution

def test_case_01():
    s = "abbaca"
    output = "ca"
    result = Solution().remove_duplicates(s)
    assert result == output


def test_case_02():
    s = "azxxzy"
    output = "ay"
    result = Solution().remove_duplicates(s)
    assert result == output
