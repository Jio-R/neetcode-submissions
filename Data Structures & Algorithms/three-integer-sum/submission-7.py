class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        import bisect
        nums.sort()
        answer = []

        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i == j:
                    continue
                
                target = 0 - n1 - n2
                bi = bisect.bisect_left(nums, target)

                if bi not in [i, j] and bi < len(nums) and nums[bi] == target:
                    check = sorted([nums[i], nums[j], nums[bi]])
                    if check not in answer:
                        print(f"Appending...\n    i = {i}\n    j = {j}\n    bi = {bi} to answer...")
                        answer.append(check)
        return answer