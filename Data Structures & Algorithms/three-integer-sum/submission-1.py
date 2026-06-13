class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []

        dp = {}

        for n in nums:
            dp[n] = dp.get(n, 0) + 1

        for n1 in nums:
            print(f"n1: {n1}")
            if dp[n1] < 1:
                    continue
            dp[n1] -= 1
            for n2 in nums:
                if dp[n2] < 1:
                    continue
                dp[n2] -= 1

                target = 0 - n1 - n2

                if target in dp and dp[n1] > 0 and dp[n2] > 0 and dp[target] > 0:
                    print("appending")
                    out.append([n1, n2, target])
                    dp[n1] -= 1
                    dp[n2] -= 1
                    dp[target] -= 1
                dp[n2] += 1
            dp[n1] += 1

        return out