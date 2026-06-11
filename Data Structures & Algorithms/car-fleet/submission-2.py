class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carInfo = sorted(list(zip(position, speed)), reverse=True)
        fleets = []
        for car in carInfo:
            if not fleets or (target-car[0])/car[1]>fleets[-1]:
                fleets.append((target-car[0])/car[1])
        return len(fleets)
        
            

        