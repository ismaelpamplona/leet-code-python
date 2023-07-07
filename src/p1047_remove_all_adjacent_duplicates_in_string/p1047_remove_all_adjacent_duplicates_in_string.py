class Solution:
    def remove_duplicates(self, s: str) -> str:
        stack: List(str) = []
        for c in s:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)