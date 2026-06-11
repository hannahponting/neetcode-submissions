class StockSpanner:

    def __init__(self):
        self.iqueue = []

    def next(self, price: int) -> int:
        span = 1
        while self.iqueue and self.iqueue[-1][0] <= price:
            span += self.iqueue[-1][1]
            self.iqueue.pop()
        self.iqueue.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)