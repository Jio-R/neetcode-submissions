class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dih = {}

        for i, num in enumerate(nums):
            if target - num in dih:
                return [dih[target-num], i]
            else:
                dih[num] = i
            