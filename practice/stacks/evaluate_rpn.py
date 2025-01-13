from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def getResult(a, b, op):
            if op == '+':
                res = int(a) + int(b)
            elif op == '-':
                res = int(a) - int(b)
            elif op == '*':
                res = int(a) * int(b)
            elif op == '/':
                res = int(int(a) / int(b))
            return res
        operators = {'+', '-', '*', '/'}
        stack = list()
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                b = stack.pop()
                a = stack.pop()
                r = getResult(a, b, t)
                stack.append(str(r))
        return int(stack[0])

# Main section
for tokens in [
                 ['2','1','+','3','*'],
                 ['4','13','5','/','+'],
                 ['10','6','9','3','+','-11','*','/','*','17','+','5','+'],
              ]:
    print(f'tokens = {tokens}')
    sol = Solution()
    r = sol.evalRPN(tokens)
    print(f'r = {r}')
    print('==================')

