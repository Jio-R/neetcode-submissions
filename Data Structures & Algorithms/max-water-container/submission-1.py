class Solution:
    def maxArea(self, heights: List[int]) -> int:
        from itertools import islice
        
        leftx, lefty = 0, heights[0]
        rightx, righty = 1, heights[1]
        answer = min(lefty, righty)
        
        for x, y in enumerate([i for i in islice(heights, 2, None)], start=2):
            print(f"x: {x}, y: {y}\n    Before: {answer}\n    leftx: {leftx}\n    lefty: {lefty}\n    rightx: {rightx}\n    righty: {righty}")
            lCandidate = (x - leftx) * min(y, lefty)
            rCandidate = (x - rightx) * min(y, righty)

            if rCandidate >= answer and righty > lefty:
                leftx, lefty = rightx, righty
                rightx, righty = x, y
                answer = rCandidate
            elif lCandidate > answer:
                rightx, righty = x, y
                answer = lCandidate
            print(f"\n    After: {answer}\n    leftx: {leftx}\n    lefty: {lefty}\n    rightx: {rightx}\n    righty: {righty}\n")
        return answer