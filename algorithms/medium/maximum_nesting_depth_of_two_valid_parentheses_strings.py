# It's difficult to figure out what the problem wants us to do, initially. But pay
# attention to the word "subsequence". We simply need to create two subsequences so
# that they have the least nesting depth. Subsequences preserve the order.
# Also check the solutions by Domii and lee215.

from typing import List

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        N = len(seq)
        stack = list()
        res = list()
        occ = 0
        for ch in seq:
            if ch == '(':
                if stack:
                    occ = (stack[-1] + 1)%2
                stack.append(occ)
                res.append(occ)
            else:
                res.append(stack.pop())
        return res

# Main section
for seq in [
              '(()())',
              '()(())()',
              '(((()())))',
              '()()()()()()()()',
              '()()()()(())()(()()((())))',
           ]:
    print(f'seq = {seq}')
    sol = Solution()
    r = sol.maxDepthAfterSplit(seq)
    print(f'r = {r}')
    print('==================')


