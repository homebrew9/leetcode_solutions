class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append([price, ans])
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

ss = StockSpanner()
res = ss.next(100)
print(res)
res = ss.next(80)
print(res)
res = ss.next(60)
print(res)
res = ss.next(70)
print(res)
res = ss.next(60)
print(res)
res = ss.next(75)
print(res)
res = ss.next(85)
print(res)


