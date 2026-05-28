class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        L = set(nums)

        for n in L:
            cur = 0
            if n - 1 not in L:
                cur = 1
                while n + cur in L:
                    cur += 1
            longest = max(cur, longest)

        return longest