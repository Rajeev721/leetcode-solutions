class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{","]":"[",")":"("}
        stack = []

        for i in s:
            if i in hashmap:
                if stack is not None and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False