from typing import List

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = list(s)
        count = 0
        for i, v in enumerate(s):
            if v == '(':
                count += 1
                if count == 1:
                    ind = i
            elif v == ')':
                count -= 1
                if count == 0:
                    arr[i] = ''
                    arr[ind] = ''
        return ''.join(arr)

# Main section
for s in [
            '(()())(())',
            '(()())(())(()(()))',
            '()()',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.removeOuterParentheses(s)
    print(f'r = {r}')
    print('=============================')

