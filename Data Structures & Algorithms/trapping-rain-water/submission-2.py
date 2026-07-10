class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1
        imax = 0
        maxTable = {}

        while i <= j:
            if height[i] > imax:
                imax = height[i]
                maxTable[i] = 0
                i+=1
                continue

            maxTable[i] = imax - height[i]
            i+=1
        
        imax = 0
        while j > 0:
            if height[j] > imax:
                imax = height[j]
                j-=1
                continue
            res += min(maxTable[j], (imax - height[j]))
            j-=1
        return res