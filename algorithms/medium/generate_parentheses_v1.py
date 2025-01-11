#
# Does not work for n = 7 and 8.
# "RecursionError: maximum recursion depth exceeded while calling a Python object"
#
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def permutations(perm, slider, i, j):
            #print(f'\tperm, slider, i, j = {perm}, {slider}, {i}, {j}')
            if j >= len(perm):
                return list(st)
            item = perm[j]
            if i >= len(item):
                return permutations(perm, slider, 0, j+1)
                #return
            if i == 0:
                #print(slider + item)
                st.add(slider + item)
            lc = item[:i]
            rc = item[i+1:]
            s1 = lc + slider[0] + item[i] + slider[1] + rc
            s2 = lc + item[i] + slider + rc
            #print(s1)
            #print(s2)
            st.add(s1)
            st.add(s2)
            return permutations(perm, slider, i+1, j)

        perm = ['()']
        slider = '()'
        i = 0
        j = 0
        for _ in range(n-1):
            st = set()
            perm = permutations(perm, slider, i, j)
            #perm = list(st)
        return perm

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.generateParenthesis(n)
    print(f'r = {r}')
    print('==========================')


