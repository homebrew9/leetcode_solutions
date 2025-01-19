class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = list()
        for ch in expression:
            if ch in ('|', '!', '&'):
                stack.append(ch)
            elif ch in ('(', ','):
                continue
            elif ch in ('f', 't'):
                if type(stack[-1]) == list:
                    stack[-1].append(False if ch == 'f' else True)
                else:
                    stack.append([False if ch == 'f' else True])
            elif ch == ')':
                arr = stack.pop()
                op = stack.pop()
                if op == '!':
                    val = not arr[0]
                elif op == '&':
                    val = arr[0]
                    for item in arr[1:]:
                        val = val & item
                elif op == '|':
                    val = arr[0]
                    for item in arr[1:]:
                        val = val | item
                if not stack or type(stack[-1]) != list:
                    stack.append([val])
                else:
                    stack[-1].append(val)
        val = stack[0]
        return val[0]

# Main section
for expression in [
                     '&(|(f))',
                     '|(f,f,f,t)',
                     '!(&(f,t))',
                     '!(!(!(!(!(!(!(&(&(&(&(&(&(|(|(|(|(|(|(|(|(|(|(f,f,f,f,f,f,f,t,t,t,t,t,t,t,t,f,t,f,t,f,t,f,t,f,t,f,t)))))))))))))))))))))))',
                     '|(&(t,f,t),!(t))',
                  ]:
    print(f'expression = {expression}')
    sol = Solution()
    r = sol.parseBoolExpr(expression)
    print(f'r = {r}')
    print('===================')


