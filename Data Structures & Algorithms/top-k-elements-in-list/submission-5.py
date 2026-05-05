class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dih = {}

        for num in nums:
            if num in dih:
                dih[num] += 1
            else:
                dih[num] = 1

        dih = sorted(dih.items(), key=lambda x: x[1])[::-1]
        
        return [i[0] for i in dih[:k]]