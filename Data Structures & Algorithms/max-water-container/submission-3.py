class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = min(heights[0], heights[-1]) * (len(heights) - 1)

        def check(L):
            nonlocal res
            match len(L):
                case 2:
                    res = max(min([L[0], L[1]]), res)
                    return None
                case 3:
                    res = max(min(L[0], L[2]) * 2, res)
                    return check([max([L[0], L[2]]), L[1]])
            
            res = max(min(L[0], L[-1]) * (len(L) - 1), res)

            if L[0] > L[-1]:
                return check(L[:-1])
            if L[0] < L [-1] or L[1] < L[-2]:
                return check(L[1:])
            return check(L[:-1])

        check(heights)
        return res
