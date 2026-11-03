class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0

        cars = []
        for i, x in enumerate(position):
            cars.append([x, speed[i]])

        cars.sort(key=lambda x: x[0])
        position = [x[0] for x in cars]
        speed = [x[1] for x in cars]

        res = 1
        lead = [position.pop(), speed.pop()]

        while position:
            second = [position.pop(), speed.pop()]
            
            if (target - second[0]) / second[1] <= (target - lead[0]) / lead[1]:
                continue
            res += 1
            lead = second
        
        return res