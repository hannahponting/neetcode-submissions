class TimeMap:

    def __init__(self):
        self.response = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.response[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.response[key]
        res = ""
        l = 0
        r = len(values)-1

        while l <= r:
            mid = (l+r)//2 
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                r = mid -1 
            else:
                l = mid + 1
                res = values[mid][1]  
        
        return res
        
