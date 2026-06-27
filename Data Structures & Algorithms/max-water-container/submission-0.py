class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftx, lefty = 0, heights[0]
        rightx, righty = 1, heights[1]
        answer = min(lefty, righty)
        
        for x, y in enumerate(heights):
            if x in [0, 1]:
                continue
            print(f"x: {x}, y: {y}\n    Before: {answer}\n    leftx: {leftx}\n    lefty: {lefty}\n    rightx: {rightx}\n    righty: {righty}")
            lCandidate = (x - leftx) * min(y, lefty)
            rCandidate = (x - rightx) * min(y, righty)

            if rCandidate >= answer and rCandidate >= lCandidate: #wrong bc if
                leftx, lefty = rightx, righty
                rightx, righty = x, y
                answer = rCandidate
            # if (x - rightx) * min(righty, y) > answer:
            #     leftx, lefty = rightx, righty
            #     rightx, righty = x, y
            #     answer = (rightx - leftx) * min(lefty, righty)
            elif lCandidate > answer:
                rightx, righty = x, y
                answer = lCandidate
            print(f"\n    After: {answer}\n    leftx: {leftx}\n    lefty: {lefty}\n    rightx: {rightx}\n    righty: {righty}\n")
            # NOTE FOR FUTURE: test case 1 fails bc 1,7,2 causes i=2 to have to pick between the wide 2 of the 1 or the tall 2 of the 7.
            # I'm thinking for now I can store the constituents for each box by Y value and pick by highest Y in case of tie.
        return answer