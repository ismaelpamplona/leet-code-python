class Solution:
    def is_valid(self, s: str) -> bool:
        hashmap = {'(': ')', '{': '}', '[': ']'}
        stack: List(str) = []
        for c in s:
            if c in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                open_bracket = stack.pop()      
                close_bracket = hashmap[open_bracket]
                if close_bracket != c:
                    return False
        return not stack
