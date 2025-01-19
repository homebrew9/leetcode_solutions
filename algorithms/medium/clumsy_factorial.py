#
# Using a stack since the order of operations is important.
#
class Solution:
    def clumsy(self, n: int) -> int:
        operations = ['*', '//', '+', '-']
        stack = list()
        stack.append(n)
        i = 0
        while n > 1:
            stack.append(operations[i])
            n -= 1
            if stack[-1] in ('*', '//'):
                op = stack.pop()
                num = stack.pop()
                if op == '*':
                    stack.append(num * n)
                else:
                    stack.append(num // n)
            else:
                stack.append(n)
            i = (i + 1) % len(operations)
        res = stack[0]
        for i in range(1, len(stack), 2):
            if stack[i] == '+':
                res += stack[i+1]
            elif stack[i] == '-':
                res -= stack[i+1]
        return res

# Main section
for n in [
            4,
            10,
            10000,
            3437,
            3599,
            103,
            101,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            7328,
            9999,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.clumsy(n)
    print(f'r = {r}')
    print('================')

            
