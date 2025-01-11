class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        factor, token = '', ''
        for ch in s:
            if ch.isdigit():
                if token:
                    stack.append(token)
                    token = ''
                factor += ch
            elif ch == '[':
                stack.append(factor)
                factor = ''
            elif ch.isalpha():
                token += ch
            elif ch == ']':
                while stack[-1].isalpha():
                    token = stack.pop() + token
                factor = stack.pop()
                tmp = token * int(factor)
                stack.append(tmp)
                factor, token = '', ''
        return ''.join(stack) + token

# Main section
for s in [
            '5[c]',
            'a5[c]',
            'a3[b2[c]]',
            'a4[b3[c2[d]]]',
            '3[a5[c]]4[b]',
            '3[z]2[2[y]pq4[2[jk]e1[f]]]ef',
            '3[a]2[bc]',
            '2[abc]3[cd]ef',
            '3[a2[c]]',
            '4[a3[b2[c]]]',
            'abcdef',
            '4[a]bcd',
            'abc4[d]',
            'abc4[d]efg',
            'abc3[p2[q]]def',
            'sd2[f2[e]g]i',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.decodeString(s)
    print(f'r = {r}')
    print('===============')



