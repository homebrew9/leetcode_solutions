class MyQueue:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, x: int) -> None:
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        # Since calls to pop are valid, there is no need to
        # check if queue is empty.
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        return False

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



