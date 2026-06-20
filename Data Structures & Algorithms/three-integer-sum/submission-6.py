class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        import bisect
        nums.sort()
        answer = []

        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i == j:
                    continue
                if i < j:
                    out = [i, j]
                else:
                    out = [j, i]
                
                target = 0 - n1 - n2
                bi = bisect.bisect_left(nums, target)

                if bi < len(nums) and nums[bi] == target and bi not in out:
                    bisect.insort(out, bi)
                    if out not in answer:
                        answer.append(out)

            del nums[0]
        
        for i, x in enumerate(answer):
            answer[i] = [nums[x[0]], nums[x[1]], nums[x[2]]]
        return answer