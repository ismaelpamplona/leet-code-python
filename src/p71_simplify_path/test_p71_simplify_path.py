from p71_simplify_path import Solution

def test_case_01():
    path = "/home/"
    output = "/home"
    result = Solution().simplify_path(path)
    assert result == output

def test_case_02():
    path = "/../"
    output = "/"
    result = Solution().simplify_path(path)
    assert result == output

def test_case_03():
    path = "/home//foo/"
    output = "/home/foo"
    result = Solution().simplify_path(path)
    assert result == output

def test_case_04():
    path = "/a/b///c/.././d/../f/"
    output = "/a/b/f"
    result = Solution().simplify_path(path)
    assert result == output