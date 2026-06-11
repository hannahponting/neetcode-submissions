class TimeMap:

    def __init__(self):
        self.time = 1
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        li = self.store[key]
        l = 0
        r = len(li)-1
        res = ""
        while l <= r:
            mid = (l+r) // 2
            if timestamp >= li[mid][0]:
                res = li[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res
