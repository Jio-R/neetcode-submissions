class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights) - 1

        while j - i > 1: # dont forget to address what will happen after j - i <= 2
            tmp = min(heights[i], heights[j]) * (j - i)
            res = max(res, tmp)
            
            if heights[j] > heights[i]:
                i += 1
                continue
            if heights[j] < heights[i] or heights[i + 1] < heights[j - 1]:
                j -= 1
                continue
            i += 1

        return res

            
