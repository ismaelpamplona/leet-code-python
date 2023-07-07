# p1047_remove_all_adjacent_duplicates_in_string
[https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string)

## Initial provided code
```Python
class Solution:
    def removeDuplicates(self, s: str) -> str:
```

## First approach - Stack

- Time complexity : $O(n)$, where $n$ is a string length.
- Space complexity : O(n−d), where $d$ is a total length
for all duplicates.