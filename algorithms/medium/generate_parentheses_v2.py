from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, ans, s):
            #print(f'\tl, r, ans, s = {l}, {r}, {ans}, {s}')
            if r < l:
                return
            if l == 0 and r == 0:
                ans.append(s)
                return
            if l > 0:
                dfs(l-1, r, ans, s+'(')
            if r > 0:
                dfs(l, r-1, ans, s+')')

        l, r, ans = n, n, []
        dfs(l, r, ans, '')
        return ans

#class Solution:
#    def generateParenthesis(self, n):
#        if not n:
#            return []
#        left, right, ans = n, n, []
#        self.dfs(left,right, ans, '')
#        return ans
#    
#    def dfs(self, left, right, ans, string):
#        if right < left:
#            return
#        if not left and not right:
#            ans.append(string)
#            return
#        if left:
#            self.dfs(left-1, right, ans, string + '(')
#        if right:
#            self.dfs(left, right-1, ans, string + ')')

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



