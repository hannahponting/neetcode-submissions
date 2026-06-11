class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, reverse=True)
        print(cars)
        fleets = []
        for car in cars:
            time_to_end = (target-car[0])/car[1]
            if not fleets or time_to_end > fleets[-1]:
                fleets.append(time_to_end)
        return len(fleets)
        