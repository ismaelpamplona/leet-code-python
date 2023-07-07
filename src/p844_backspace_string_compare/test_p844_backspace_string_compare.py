from p844_backspace_string_compare import Solution

def test_case_01():
    s = "ab#c"
    t = "ad#c"
    result = Solution().backspace_compare(s, t)
    assert result == True

def test_case_02():
    s = "ab##"
    t = "c#d#"
    result = Solution().backspace_compare(s, t)
    assert result == True

def test_case_03():
    s = "a#c"
    t = "b"
    result = Solution().backspace_compare(s, t)
    assert result == False

def test_case_04():
    s = "y#fo##f"
    t = "y#f#o##f"
    result = Solution().backspace_compare(s, t)
    assert result == True    
