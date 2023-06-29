import math
from typing import List
class Solution:
    def get_averages_prefix(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        result = [-1] * len(nums)
        if (2 * k + 1 > len(nums)):
            return result
        prefix = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        els = k * 2 + 1
        for i in range(k * 2, len(nums)):
            sum = prefix[i + 1] - prefix[i - (2 * k)]
            avg = math.floor(sum / els)
            result[i - k] = avg
        return result
        

    def get_averages_sliding(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        result = [-1] * len(nums)
        if (2 * k + 1 > len(nums)):
            return result
        sum = 0
        els = k * 2 + 1
        for i in range(0, len(nums)):
            sum += nums[i]
            start_pos = i - (k * 2)
            if start_pos >= 0:
                if start_pos > 0:
                    sum -= nums[start_pos - 1]
                avg = math.floor(sum / els)
                result[i - k] = avg
        return result