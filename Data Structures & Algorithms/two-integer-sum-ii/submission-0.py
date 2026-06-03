class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from bisect import bisect_left

        for i, x in enumerate(numbers):
            for j, y in enumerate (numbers):
                if x + y == target:
                    return [i+1, j+1]