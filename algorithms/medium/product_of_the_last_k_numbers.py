class ProductOfNumbers:
    def __init__(self):
        self.pfx = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.pfx = [1]
            self.size = 0
        else:
            last_num = self.pfx[-1]
            self.pfx += [last_num * num]
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return self.pfx[-1] // self.pfx[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# Test cases
# ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
# [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
