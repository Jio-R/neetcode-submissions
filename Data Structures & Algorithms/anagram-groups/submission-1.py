class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

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
            
        output = [[strs[0]]]

        for s in strs[1:]:
            found = False
            for o in output:
                if isAnagram(self, o[0], s):
                    found = True
                    o.append(s)
                    break
            if not found:
                output.append([s])

        return output