class MyCircularDeque:
    def __init__(self, k: int):
        self.arr = [None for _ in range(k)]
        self.head = None
        self.tail = None
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.arr[0] = value
            self.head = self.tail = 0
            return True
        self.head = self.size - 1 if self.head == 0 else self.head  - 1
        self.arr[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.arr[0] = value
            self.head = self.tail = 0
            return True
        self.tail = (self.tail + 1) % self.size
        self.arr[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = None
            return True
        self.head = (self.head + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = None
            return True
        self.tail = self.size - 1 if self.tail == 0 else self.tail - 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.tail]

    def isEmpty(self) -> bool:
        return self.head is None and self.tail is None

    def isFull(self) -> bool:
        if self.isEmpty():
            return False
        return (self.tail + 1) % self.size == self.head

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

for arr_ops, arr_param, arr_exp in [
         (['MyCircularDeque','insertLast','insertLast','insertFront','insertFront','getRear','isFull','deleteLast','insertFront','getFront'], [[3],[1],[2],[3],[4],[],[],[],[4],[]], [None,True,True,True,False,2,True,True,True,4]),
    ]:
    print(f'arr_ops, arr_param, arr_exp = {arr_ops}, {arr_param}, {arr_exp}')
    for ops, param, exp in zip(arr_ops, arr_param, arr_exp):
        if ops == 'MyCircularDeque':
            print(f'{ops}{param}')
            obj = MyCircularDeque(param[0])
        elif ops == 'insertFront':
            print(f'{ops}{param}')
            r = obj.insertFront(param[0])
            print(f'r, exp = {r}, {exp}')
            assert(r == exp)
        elif ops == 'insertLast':
            print(f'{ops}{param}')
            r = obj.insertLast(param[0])
            print(f'r, exp = {r}, {exp}')
            assert(r == exp)
        elif ops == 'deleteFront':
            print(f'{ops}{param}')
            r = obj.deleteFront()
            print(f'r, exp = {r}, {exp}')
            assert(r == exp)
        elif ops == 'deleteLast':
            print(f'{ops}{param}')
            r = obj.deleteLast()
            print(f'r, exp = {r}, {exp}')
            assert(r == exp)
        elif ops == 'getFront':
            print(f'{ops}{param}')
            r = obj.getFront()
            print(f'r, exp = {r}, {exp}')
            assert(r == exp)
        elif ops == 'getRear':
            print(f'{ops}{param}')
            r = obj.getRear()
            print(f'r, exp = {r}, {exp}')
            assert(r == exp)
        elif ops == 'isEmpty':
            print(f'{ops}{param}')
            r = obj.isEmpty()
            print(f'r, exp = {r}, {exp}')
            assert(r == exp)
        elif ops == 'isFull':
            print(f'{ops}{param}')
            r = obj.isFull()
            print(f'r, exp = {r}, {exp}')
            assert(r == exp)
        print('~~~~~~~')
    print('=====================')


