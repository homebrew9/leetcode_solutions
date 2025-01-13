class Solution:
    def isValid(self, s: str) -> bool:
        hsh1 = { '(': ')', '{': '}', '[': ']' }
        hsh2 = { ')': '(', '}': '{', ']': '[' }
        stack = list()
        for ch in s:
            if ch in hsh1:
                stack.append(ch)
            else:
                if len(stack) == 0 or stack[-1] != hsh2[ch]:
                    return False
                stack.pop()
        if len(stack) > 0:
            return False
        else:
            return True

# Main section
for s in [
            '()',
            '()[]{}',
            '(]',
            '((()))[[{}{}]]',
            '((()))[[{}{}]]{{}',
            ']',
            '{',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.isValid(s)
    print(f'r = {r}')
    print('===================')

