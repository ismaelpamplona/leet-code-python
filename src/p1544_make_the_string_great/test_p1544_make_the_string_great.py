from p1544_make_the_string_great import Solution

def test_case_01():
    s = "leEeetcode"
    output = "leetcode"
    result = Solution().make_good(s)
    assert result == output

def test_case_02():
    s = "abBAcC"
    output = ""
    result = Solution().make_good(s)
    assert result == output    

def test_case_03():
    s = "s"
    output = "s"
    result = Solution().make_good(s)
    assert result == output