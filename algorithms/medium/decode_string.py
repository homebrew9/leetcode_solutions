class Solution:
    def decodeString(self, s: str) -> str:
        stack = ['']
        n = 0 
        for ch in s:
            if ch.isdigit():
                print(f'\t{ch} is a digit')
                if n == 0:
                    n = int(ch)
                else:
                    n = 10 * n + int(ch)
            elif ch.isalpha():
                print(f'\t{ch} is alpha')
                stack[-1] += ch
            elif ch == '[':
                print(f'\t{ch} is [')
                stack.append(n)
                stack.append('')
                n = 0
            elif ch == ']':
                print(f'\t{ch} is ]')
                token = stack.pop()
                rep = stack.pop()
                pre = stack.pop()
                stack.append(pre + (token * rep))
            print(f'\t\tstack = {stack}')
        return stack[0]

# Main section
for s in [
            '3[a]2[bc]',
            '3[a2[c]]',
            '2[abc]3[cd]ef',
            '5[a4[b3[c2[d]]]]',
            '3[a4[b5[d]e]c]',
            '100[leetcode]',
            '123[ab]',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.decodeString(s)
    print(f'r = {r}')
    print('==============')

