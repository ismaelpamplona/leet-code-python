from p20_valid_parentheses import Solution

def test_case_01():
    s = "()"
    result = Solution().is_valid(s)
    assert result == True

def test_case_02():
    s = "()[]{}"
    result = Solution().is_valid(s)
    assert result == True

def test_case_03():
    s = "(]"
    result = Solution().is_valid(s)
    assert result == False

def test_case_04():
    s = "{[]}"
    result = Solution().is_valid(s)
    assert result == True    

def test_case_05():
    s = "([)]"
    result = Solution().is_valid(s)
    assert result == False      