from collections import deque
from typing import List
class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        ans: List[int] = []
        q = deque()

        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)

            if q[0] + k == i:
                q.popleft()

            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans
