class MinStack:
    def __init__(self):
        self.arr = list()

    def push(self, val: int) -> None:
        min_val = val
        if len(self.arr) > 0 and (n := self.arr[-1][1]) < min_val:
                min_val = n
        self.arr.append((val, min_val))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()

arr1 = ['push','push','push','getMin','pop','top','getMin']
arr2 = [[-2],[0],[-3],[],[],[],[]]
res = list()
for op, arr in zip(arr1, arr2):
    if op == 'push':
        r = obj.push(arr[0])
        res.append(r)
        #print(f'r = {r}')
    elif op == 'pop':
        r = obj.pop()
        res.append(r)
        #print(f'r = {r}')
    elif op == 'top':
        r = obj.top()
        res.append(r)
        #print(f'r = {r}')
    elif op == 'getMin':
        r = obj.getMin()
        res.append(r)
        #print(f'r = {r}')
print(res)
print('===========')

