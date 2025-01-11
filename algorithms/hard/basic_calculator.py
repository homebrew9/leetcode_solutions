class Solution:
    def calculate(self, s: str) -> int:
        # Iterate through the string and add tokens to a stack. If ')'
        # is encountered then pop all elements till the first '(' character, and
        # evaluate the result and push it back to the stack. Do this until the
        # string is processed and the stack is empty.
        # Function getResult() evaluates the expression in the input array.
        def getResult(arr):
            ans = 0
            op = None
            for elem in arr:
                if elem == '+':
                    op = '+'
                elif elem == '-':
                    op = '-'
                else:
                    if op == '+':
                        ans += int(elem)
                        op = None
                    elif op == '-':
                        ans -= int(elem)
                        op = None
                    else:
                        ans = int(elem)
            return ans

        stack = []
        curr = ''
        for ch in s:
            if ch == ' ':
                continue
            if ch == ')':
                arr = []
                if curr != '':
                    arr.append(curr)
                    curr = ''
                while True:
                    token = stack.pop()
                    if token == '(':
                        res = getResult(arr[::-1])
                        stack.append(str(res))
                        break
                    else:
                        arr.append(token)
            elif '0' <= ch <= '9':
                curr += ch
            else:
                if curr != '':
                    stack.append(curr)
                    curr = ''
                stack.append(ch)
            #print(f'\tch, stack = {ch}, {stack}')

        if curr != '':
            stack.append(curr)
            curr = None
        if len(stack) == 1:
            val = stack.pop()
            return int(val)
        else:
            arr = []
            while True:
                token = stack.pop()
                arr.append(token)
                if len(stack) == 0:
                    res = getResult(arr[::-1])
                    break
            return int(res)

# Main section
for s in [
            '1 + 1',
            ' 2-1 + 2 ',
            '(1+(4+5+2)-3)+(6+8)',
            '(1+(2+(3+(4-(3-(4-(5 - 6)))))))',
            '(1+(2+(3+(4-(3-(4-(5 + 6) - 7) - 8) - 9) - 10) - 11) - 98)',
            '1234 + 4567 - 3489 - (298 - 947 + (786 + 543) - 401)'
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.calculate(s)
    print(f'r = {r}')
    assert(eval(s) == r)
    print('=================')

