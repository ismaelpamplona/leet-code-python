from p2090_k_radius_subarray_averages import Solution

def test_01():
    nums = [7,4,3,9,1,8,5,2,6]
    output = [-1,-1,-1,5,4,4,-1,-1,-1]
    result1 = Solution().get_averages_prefix(nums, 3)
    result2 = Solution().get_averages_sliding(nums, 3)
    assert result1 == output
    assert result2 == output

def test_02():
    nums = [100000]
    output = [100000]
    result1 = Solution().get_averages_prefix(nums, 0)
    result2 = Solution().get_averages_sliding(nums, 0)
    assert result1 == output
    assert result2 == output


def test_03():
    nums = [8]
    output = [-1]
    result1 = Solution().get_averages_prefix(nums, 100000)
    result2 = Solution().get_averages_sliding(nums, 100000)
    assert result1 == output    
    assert result2 == output    
