class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info = []
        for i in range(len(position)):
            car_info.append((position[i], speed[i]))

        sorted_car_info = sorted(car_info, reverse=True)
        print(sorted_car_info)
        fleets = []
        for i in range(len(sorted_car_info)):
            time = (target - sorted_car_info[i][0])/sorted_car_info[i][1]
            print(time)
            if not fleets or time > fleets[-1]:
                fleets.append(time)

        print(fleets)
        return len(fleets)
            
            

        