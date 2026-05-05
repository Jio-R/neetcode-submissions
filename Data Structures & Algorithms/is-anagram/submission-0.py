class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dih1 = {}
        for c in s:
            if c in dih1:
                dih1[c] +=1
            else:
                dih1[c] = 1
        dih2 = {}
        for c in t:
            if c in dih2:
                dih2[c] +=1
            else:
                dih2[c] = 1
        if dih1 == dih2:
            return True
        return False