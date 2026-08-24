class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [[0, temperatures[0]]]

        for i, n in enumerate(temperatures):
            if i == 0:
                continue
            while stack and n > stack[-1][1]:
                print(stack[-1][1])
                tmp = stack.pop()
                print(tmp)
                res[tmp[0]] = i - tmp[0]
            stack.append([i, n])
        
        return res