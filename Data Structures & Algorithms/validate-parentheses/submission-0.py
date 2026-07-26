class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        left = set(['(', '{', '['])
        right = set([')', '}', ']'])

        for c in s:
            if c in left:
                count -= 1
                continue
            if c in right:
                count +=1
        
        if count == 0:
            return True
        return False