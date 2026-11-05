class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0])

        res = 1
        lead = len(cars) - 1
        second = lead - 1

        while second >= 0:
            if (target - cars[second][0]) / cars[second][1] <= (target - cars[lead][0]) / cars[lead][1]:
                second -= 1
                continue
            res += 1
            lead = second
            second -= 1

        return res
        