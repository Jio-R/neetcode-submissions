class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            cutoff = target - num

            while numbers[-1] > cutoff:
                del numbers[-1]

            if num + numbers[-1] == target:
                return [i+1, len(numbers)]
