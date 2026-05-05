class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dih = {}
        for num in nums:
            if num in dih:
                return True
            else:
                dih[num] = 0
        return False