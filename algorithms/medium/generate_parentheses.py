from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def permutations(perm, slider):
            st = set()
            for item in perm:
                st.add(slider + item)
                for i, v in enumerate(item):
                    lc = item[:i]
                    rc = item[i+1:]
                    s1 = lc + slider[0] + v + slider[1] + rc
                    s2 = lc + v + slider + rc
                    st.add(s1)
                    st.add(s2)
            return list(st)

        perm = ['()']
        slider = '()'
        for _ in range(n-1):
            perm = permutations(perm, slider)
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
    print(f'len(r) = {len(r)}')
    print('==========================')

