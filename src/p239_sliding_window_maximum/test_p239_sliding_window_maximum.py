from p239_sliding_window_maximum import Solution

def test_case_01():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    output = [3, 3, 5, 5, 6, 7]
    result = Solution().max_sliding_window(nums, k)
    assert result == output

def test_case_02():
    nums = [1]
    k = 1
    output = [1]
    result = Solution().max_sliding_window(nums, k)
    assert result == output