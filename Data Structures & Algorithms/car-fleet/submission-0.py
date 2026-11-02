class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not speed:
            return 0

        res = 1
        lead = [position.pop(), speed.pop()]

        while position:
            second = [position.pop(), speed.pop()]
            if (target - second[0]) / second[1] > (target - lead[0]) / lead[1]:
                res += 1
        
        return res