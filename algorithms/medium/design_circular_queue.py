class MyCircularQueue:
    def __init__(self, k: int):
        self.limit = k
        self.cq = list()

    def enQueue(self, value: int) -> bool:
        if len(self.cq) < self.limit:
            self.cq.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if len(self.cq) > 0:
            del self.cq[-1]
            return True
        else:
            return False

    def Front(self) -> int:
        if len(self.cq) > 0:
            return self.cq[0]
        else:
            return -1

    def Rear(self) -> int:
        if len(self.cq) > 0:
            return self.cq[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.cq) == 0

    def isFull(self) -> bool:
        return len(self.cq) == self.limit

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# Main section
#  mcq = MyCircularQueue(3)
#  r = mcq.enQueue(1); # return True
#  print(f'r = {r}')
#  r = mcq.enQueue(2); # return True
#  print(f'r = {r}')
#  r = mcq.enQueue(3); # return True
#  print(f'r = {r}')
#  r = mcq.enQueue(4); # return False
#  print(f'r = {r}')
#  r = mcq.Rear();     # return 3
#  print(f'r = {r}')
#  r = mcq.isFull();   # return True
#  print(f'r = {r}')
#  r = mcq.deQueue();  # return True
#  print(f'r = {r}')
#  r = mcq.enQueue(4); # return True
#  print(f'r = {r}')
#  r = mcq.Rear();     # return 4
#  print(f'r = {r}')
#  print('===================================')

#["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","deQueue","deQueue","isEmpty","isEmpty","Rear","Rear","deQueue"]
#[[8],              [3],      [9],      [5],      [0],      [],       [],        [],       [],      [],    [],    []]

mcq = MyCircularQueue(8)
r = mcq.enQueue(3)
print(f'r = {r}')
r = mcq.enQueue(9)
print(f'r = {r}')
r = mcq.enQueue(5)
print(f'r = {r}')
r = mcq.enQueue(0)
print(f'r = {r}')
r = mcq.deQueue()
print(f'r = {r}')
r = mcq.deQueue()
print(f'r = {r}')
r = mcq.isEmpty()
print(f'r = {r}')
r = mcq.isEmpty()
print(f'r = {r}')
r = mcq.Rear()
print(f'r = {r}')
r = mcq.Rear()
print(f'r = {r}')
r = mcq.deQueue()
print(f'r = {r}')
print('===================================')

