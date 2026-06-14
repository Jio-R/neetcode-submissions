class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        
        dp = {}
        for n in nums:
            dp[n] = dp.get(n, 0) + 1

        for n1 in nums:
            if dp[n1] < 1:
                    continue
            dp[n1] -= 1

            for n2 in nums:
                # if dp[n1] < 1:
                #     continue
                if dp[n2] < 1:
                    continue
                dp[n2] -= 1

                target = 0 - n1 - n2

                if dp.get(target, 0) > 0:
                    dp[target] -= 1
                    out.append([n1, n2, target])
                else:
                    dp[n1] += 1
                    dp[n2] += 1

        return out