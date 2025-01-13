# A little bit modified algorithm.
class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        num, chunk = '', ''
        for c in s:
            #print(c, stack)
            if c.isdigit():
                if len(chunk) > 0:
                    if stack and stack[-1].isalpha():
                        stack[-1] += chunk
                    else:
                        stack.append(chunk)
                    chunk = ''
                num += c
            elif c.isalpha():
                chunk += c
            elif c == '[':
                stack.append(num)
                num = ''
            elif c == ']':
                if len(chunk) > 0:
                    if stack and stack[-1].isalpha():
                        chunk = stack.pop() + chunk
                else:
                    chunk = stack.pop()
                num = stack.pop()
                tmp = chunk * int(num)
                if stack and stack[-1].isalpha():
                    stack[-1] += tmp
                else:
                    stack.append(tmp)
                num, chunk = '', ''
        return ''.join(stack) + chunk

# Main section
for s in [
            '3[a]2[bc]',
            '3[a2[c]]',
            '2[abc]3[cd]ef',
            '100[leetcode]',
            '3[z]2[2[y]pq4[2[jk]e1[f]]]ef',
            '3[z]2[2[y]pq4[2[jk]e1[f]]]ef',
            'sd2[f2[e]g]i',
            '2[a3[c4[e5[g6[i7[k]l]j]h]f]d]b',
            'ab2[cd3[ef4[gh5[ij]kl]mn]op]qr',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.decodeString(s)
    print(f'r = {r}')
    print('======================')


