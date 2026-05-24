class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
            
        L = [False] * (max(nums)+1)
        
        for n in nums:
            L[n] = True
        print(f"L: {[[i, L[i]] for i, val in enumerate(L)]}")

        last = L[0]
        if last:
            cur = 1
        else:
            cur = 0
        longest = 0

        for n in L[1:]:
            if n:
                cur += 1
                longest = max(cur, longest)
            else:
                longest = max(cur, longest)
                cur = 0

        return longest