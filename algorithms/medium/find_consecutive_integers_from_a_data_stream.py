class DataStream:

    def __init__(self, value: int, k: int):
        self.arr = list()
        self.value = value
        self.k = k
        self.streak = 0

    def consec(self, num: int) -> bool:
        self.arr.append(num)
        if self.arr[-1] == self.value:
            self.streak += 1
        else:
            self.streak = 0
        print(f'\tstreak, arr = {self.streak}, {self.arr}')
        if self.streak >= self.k:
            return True
        else:
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

value = 4
k = 1
obj = DataStream(value, k)
print(obj)

arr = [[3],[5],[4],[4],[3],[4],[3],[5]]
for item in arr:
    num = item[0]
    param_1 = obj.consec(num)
    print(param_1)

#[false,false,true,true,false,true,false,false]

