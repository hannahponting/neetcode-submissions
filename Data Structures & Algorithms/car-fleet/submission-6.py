class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for car in range(len(position)):
            cars.append((position[car], speed[car]))
        cars = sorted(cars, reverse=True)
        
        fleets = []
        print(cars)
        for position, speed in cars:
            time = (target-position) / speed
            if not fleets or time> fleets[-1]:
                fleets.append(time)
        return len(fleets)