from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def getResult(arr):
            res = None
            if arr[1] == '+':
                res = int(arr[2]) + int(arr[0])
            elif arr[1] == '-':
                res = int(arr[2]) - int(arr[0])
            elif arr[1] == '*':
                res = int(arr[2]) * int(arr[0])
            elif arr[1] == '/':
                res = int(int(arr[2]) / int(arr[0]))
            return res

        stack = list()
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                arr = list()
                arr.append(stack.pop())
                arr.append(t)
                arr.append(stack.pop())
                stack.append(getResult(arr))
            else:
                stack.append(t)
        return int(stack[0])

# Main section
for tokens in [
                 ['2','1','+','3','*'],
                 ['4','13','5','/','+'],
                 ['10','6','9','3','+','-11','*','/','*','17','+','5','+'],
                 ['18']
              ]:
    print(f'tokens = {tokens}')
    sol = Solution()
    r = sol.evalRPN(tokens)
    print(f'r = {r}')
    print('======================')

