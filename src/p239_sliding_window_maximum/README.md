# p239_sliding_window_maximum
[https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

## Initial provided code
```Python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
```

## First approach - Monotonic Stack
- n: number of nums elements
- k: sliding window size
- time complexity: $O(2n) = O(n)$
- space complexity: $O(k)$

