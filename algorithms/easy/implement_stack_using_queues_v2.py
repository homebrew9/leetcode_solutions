#
# Here, we maintain the stack in reverse order!
#
from collections import deque

class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Main section
myStack = MyStack();
print(f'myStack = {myStack}')
r = myStack.push(1);
print(f'r = {r}')
r = myStack.push(2);
print(f'r = {r}')
r = myStack.top();   # return 2
print(f'r = {r}')
r = myStack.pop();   # return 2
print(f'r = {r}')
r = myStack.empty(); # return False
print(f'r = {r}')



