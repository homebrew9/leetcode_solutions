#
# Correct DP solution very well explained by NeetCode on Youtube.
#
from typing import List
from functools import cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        @cache
        def solve(i):
            if i == len(s):
                return 0
            res = 1 + solve(i+1) # skip current char
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    res = min(res, solve(j+1))
            return res
        return solve(0)

# Main section
for s, dictionary in [
                        ('azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf', ['na','i','edd','wobow','kecv','b','n','or','jj','zul','vk','yeb','qnfac','azv','grtjba','yswmjn','xowio','u','xi','pcmatm']),
                        ('leetscode', ['leet','code','leetcode']),
                        ('sayhelloworld', ['hello','world']),
                        ('dwmodizxvvbosxxw', ['ox','lb','diz','gu','v','ksv','o','nuq','r','txhe','e','wmo','cehy','tskz','ds','kzbu']),
                        ('leetscode', ['leet','code','leetcode']),
                        ('sayhelloworld', ['hello','world']),
                        ('abcde', ['ab','abcd','cde']),
                        ('metzeaencgpgvsckjrqafkxgyzbe', ['zdzz','lgrhy','r','ohk','zkowk','g','zqpn','anoni','ka','qafkx','t','jr','xdye','mppc','bqqb','encgp','yf','vl','ctsxk','gn','cujh','ce','rwrpq','tze','zxhg','yzbe','c','o','hnk','gv','uzbc','xn','kk','ujjd','vv','mxhmv','ugn','at','kumr','ensv','x','uy','gb','ae','jljuo','xqkgj']),
                        ('azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf', ['na','i','edd','wobow','kecv','b','n','or','jj','zul','vk','yeb','qnfac','azv','grtjba','yswmjn','xowio','u','xi','pcmatm','maqnv']),
                        ('dwmodizxvvbosxxw', ['ox','lb','diz','gu','v','ksv','o','nuq','r','txhe','e','wmo','cehy','tskz','ds','kzbu']),
                        ('enknouowgowcipfipojlrpuowgoiogiiebfjiafwksaigjyd', ['gw','lq','yzqch','sah','giieb','kfqczw','qxqz','jb','ucxmpe','hpwr','y','vzlhe','i','kn','ip','iafwk','zl','dw','yhxeqi','egktb','xasq','f','c','vrllz','p','uowgo','pgxd','gnjgkm','rnug','sa','vfccq','j']),
                     ]:
    print(f's, dictionary = {s}, {dictionary}')
    sol = Solution()
    r = sol.minExtraChar(s, dictionary)
    print(f'r = {r}')
    print('==================')


