class Solution:
    def make_good(self, s: str) -> str:
        stack: List(str) = []
        for c in s:
            l = len(stack)
            if l > 0 and stack[l - 1] == c.lower() and c.isupper():
                stack.pop()
            elif l > 0 and stack[l - 1] == c.upper() and c.islower():
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)