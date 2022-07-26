class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        prt = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in prt:
                stack += char
            else:
                if not stack:
                    return False
                element = stack.pop()
                if prt[element] != char:
                    return False
        if stack:
            return False

        return True
            
