from typing import List

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lower_bound = float('-inf')
        stack = list()
        for n in preorder:
            if n <= lower_bound:
                return False
            while len(stack) > 0 and n > stack[-1]:
                lower_bound = stack.pop()
            stack.append(n)
        return True

# Main section
for preorder in [
                   [5,2,1,3,6],
                   [5,2,6,1,3],
                   [4,2,1,3,6,5,7],
                   [8,4,2,1,3,6,5,7,12,10,9,11,14,13,15],
                   [5,2,1,10,6],
                ]:
    print(f'preorder = {preorder}')
    sol = Solution()
    r = sol.verifyPreorder(preorder)
    print(f'r = {r}')
    print('==================')




