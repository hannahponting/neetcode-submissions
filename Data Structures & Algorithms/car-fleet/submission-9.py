class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for car in range(len(position)):
            cars.append((position[car],speed[car]))

        cars = sorted(cars, reverse=True)
        print(cars)
        fleets = []
        for car in cars:
            if fleets and fleets[-1] >= (target-car[0])/car[1]:
                continue
            else:
                fleets.append((target-car[0])/car[1])
        print(fleets)
        return len(fleets)

