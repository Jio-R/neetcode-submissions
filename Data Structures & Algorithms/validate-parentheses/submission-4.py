class Solution:
    def isValid(self, s: str) -> bool:
        close = {')': '(', '}': '{', ']': '['}
        right = set([')', '}', ']'])

        if s[0] in right:
            return False

        stack = [s[0]]  

        for i in range(1, len(s)):
            if s[i] in right:
                if stack == []:
                    return False
                if stack.pop() == close[s[i]]:
                    continue
            stack.append(s[i])
        if stack == []:
            return True
        return False