class MyQueue:
    def __init__(self):
        self.queue = list()

    def push(self, x: int) -> None:
        self.queue.insert(0, x)

    def pop(self) -> int:
        val = self.queue[-1]
        del self.queue[-1]
        return val

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Main section
myq = MyQueue();
print(f'myq = {myq}')
r = myq.push(1);  # queue is: [1]
print(f'r = {r}')
r = myq.push(2);  # queue is: [1, 2] (leftmost is front of the queue)
print(f'r = {r}')
r = myq.peek();   # return 1
print(f'r = {r}')
r = myq.pop();    # return 1, queue is [2]
print(f'r = {r}')
r = myq.empty();  # return False
print(f'r = {r}')
print('=========================')

myq1 = MyQueue();
print(f'myq1 = {myq1}')
r = myq1.push(1);  # queue is: [1]
print(f'r = {r}')
r = myq1.push(2);  # queue is: [1,2] (leftmost is front of the queue)
print(f'r = {r}')
r = myq1.push(3);  # queue is: [1,2,3] (leftmost is front of the queue)
print(f'r = {r}')
r = myq1.push(4);  # queue is: [1,2,3,4] (leftmost is front of the queue)
print(f'r = {r}')
r = myq1.push(5);  # queue is: [1,2,3,4,5] (leftmost is front of the queue)
print(f'r = {r}')
r = myq1.peek();   # return 1
print(f'r = {r}')
r = myq1.pop();    # return 1, queue is [2,3,4,5]
print(f'r = {r}')
r = myq1.empty();  # return False
print(f'r = {r}')
r = myq1.pop();    # return 2, queue is [3,4,5]
print(f'r = {r}')
r = myq1.pop();    # return 3, queue is [4,5]
print(f'r = {r}')
r = myq1.pop();    # return 4, queue is [5]
print(f'r = {r}')
r = myq1.pop();    # return 5, queue is []
print(f'r = {r}')
r = myq1.empty();  # return True
print(f'r = {r}')
print('=========================')


