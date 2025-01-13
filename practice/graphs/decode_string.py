#
# This is similar to Iterative DFS method that uses a stack. I think this can be solved using recursion as well.
#
class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        multiplier, chunk = '', ''
        for ch in s:
            #print(f'\tch, stack = {ch}, {stack}')
            if ch.isdigit():
                if chunk:
                    stack.append(chunk)
                    chunk = ''
                multiplier += ch
            elif ch.isalpha():
                chunk += ch
            elif ch == '[':
                stack.append(multiplier)
                multiplier = ''
            elif ch == ']':
                while stack[-1].isalpha():
                    chunk = stack.pop() + chunk
                multiplier = stack.pop()
                stack.append(chunk * int(multiplier))
                multiplier, chunk = '', ''
            #print(f'\t\tch, stack, multiplier, chunk = {ch}, {stack}, {multiplier}, {chunk}')
        return ''.join(stack) + chunk


# Main section
for s in [
            '3[a]2[bc]',
            '3[a2[c]]',
            '2[abc]3[cd]ef',
            '2[a]',
            '3[b2[a]]',
            '4[c3[b2[a]]]',
            '5[d4[c3[b2[a]]]]',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.decodeString(s)
    print(f'r = {r}')
    print('=================')


