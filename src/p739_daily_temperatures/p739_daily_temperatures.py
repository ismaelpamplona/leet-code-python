from typing import List
class Solution:
    def daily_temperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []
        for i in range(len(temps)):
            while stack and temps[stack[-1]] < temps[i]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans

