class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        L = set(nums)

        for n in nums:
            if n - 1 not in nums:
                cur = 1
                while n + cur in nums:
                    cur += 1
            longest = max(cur, longest)

        return longest