class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # O(1)
        dic = { # O(1)
            '(': ')',
            '{': '}',
            '[': ']'
        }

        if len(s) < 2: # O(1)
            return False # O(1)

        for ch in s:
            if ch in dic: # O(1)
                stack.append(ch) # O(1)
            elif len(stack) == 0 or dic[stack.pop()] != ch: # O(1)
                return False # O(1)

        return len(stack) == 0 # O(1)
