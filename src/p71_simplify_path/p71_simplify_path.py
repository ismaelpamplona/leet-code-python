class Solution:
    def simplify_path(self, path: str) -> str:
        stack: List(str) = []
        parts = path.split("/")
        for c in parts:
            if c != "." and c != ".." and c != "":
                stack.append(c)
            elif c == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)