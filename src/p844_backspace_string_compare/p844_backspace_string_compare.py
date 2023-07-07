class Solution:
    def backspace_compare(self, s: str, t: str) -> bool:
        def build(s1: str) -> str:
            stack: List(str) = []
            for c in s1:
                if c == '#':
                    stack.pop()
                else:
                    stack.append(c)

            return ''.join(stack)

        return build(s) == build(t)