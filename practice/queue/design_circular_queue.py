class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = [None] * k
        self.k = k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        # If queue is full, we cannot enqueue
        if self.isFull():
            return False
        # If queue is empty, set the first element
        if self.isEmpty():
            self.arr[0]

        

    def deQueue(self) -> bool:
        

    def Front(self) -> int:
        

    def Rear(self) -> int:
        

    def isEmpty(self) -> bool:
        if self.head is None and self.tail is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.isEmpty():
            return False
        if (self.tail + 1)%self.k == self.head:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]
# 
# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4

# Main section
for cmd, val, out in [
                       (
                          ['MyCircularQueue', 'enQueue', 'enQueue', 'enQueue', 'enQueue', 'Rear', 'isFull', 'deQueue', 'enQueue', 'Rear'],
                          [[3], [1], [2], [3], [4], [], [], [], [4], []],
                          [None, True, True, True, False, 3, True, True, True, 4],
                       ),
                    ]:
    print(f'cmd = {cmd}')
    print(f'val = {val}')
    print(f'out = {out}')
    for c, v, o in zip(cmd, val, out):
        print(f'\tc, v = {c}, {v}')
        r = None
        if c == 'MyCircularQueue':
            mcq = MyCircularQueue(val)
        elif c == 'enQueue':
            r = mcq.enQueue(val)
        elif c == 'deQueue':
            r = mcq.deQueue()
        elif c == 'Front':
            r = mcq.Front()
        elif c == 'Rear':
            r = mcq.Rear()
        elif c == 'isEmpty':
            r = mcq.isEmpty()
        elif c == 'isFull':
            r = mcq.isFull()
        print(f'\tr, o = {r}, {o}')
        print('=====')
    print('~~~~~~~~~~~~~~~~')


