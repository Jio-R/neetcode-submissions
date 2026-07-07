class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1

        while height[j] <= height[j - 1]:
            j -= 1

        while j - i > 0:
            curBucket = 0

            while height[i] <= height[i + 1]:
                i += 1

            lefty = height[i]
            i += 1
            
            while height[i] < lefty:
                curBucket += lefty - height[i]
                i += 1
            res += curBucket
            
        return res