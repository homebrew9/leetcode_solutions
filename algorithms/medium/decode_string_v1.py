class Solution:
    def decodeString(self, s: str) -> str:
        # Key thing to realize is that each pattern is of form: "prevString - num - currString"
        # E.g. 'a5[c]' => a = prev, 5 = num, c = curr
        # At '[', we insert in stack and at ']' we pop and compute new currString
        currString, currNum = '', 0
        stack = list()
        for c in s:
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            elif c.isalpha():
                currString += c
            elif c == '[':
                stack.append(currString)
                stack.append(currNum)
                currString, currNum = '', 0
            elif c == ']':
                n = stack.pop()
                prev = stack.pop()
                currString = prev + n * currString
        return currString

# Main section
for s in [
            '5[c]',
            'a5[c]',
            'a3[b2[c]]',
            'a4[b3[c2[d]]]',
            '3[a5[c]]4[b]',
            '3[z]2[2[y]pq4[2[jk]e1[f]]]ef',
         ]:
    print(f's = {s}')
    r = decodeString(s)
    print(f'r = {r}')
    print('===============')


