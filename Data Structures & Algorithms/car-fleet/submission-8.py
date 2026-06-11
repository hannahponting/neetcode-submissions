class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, reverse=True)

        fleets = []
        print(cars)
        for car_position, car_speed in cars:
            time = (target-car_position)/car_speed
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)
