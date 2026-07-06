class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights) - 1

        while j - i > 0:
            tmp = min(heights[i], heights[j]) * (j - i)
            res = max(res, tmp)
            
            if heights[j] > heights[i]:
                i += 1
                continue
            if heights[j] < heights[i]:
                j -= 1
                continue
            i += 1
            j -= 1
        
        return res
        