class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_position = sorted(zip(position, speed), reverse=True)
        fleets = []
        print(speed_position)
        for position, speed in speed_position:
            time_to_end = (target-position)/speed
            if not fleets:
                fleets.append(time_to_end)
            elif fleets[-1]<time_to_end:
                fleets.append(time_to_end)
        return len(fleets)
