#
# Incorrect solution. Does not work for the test case: ('abcde', ['ab','abcd','cde']).
# The code here returns 1 but the correct answer is 0.
# Check the DP solution in version 1
#
from typing import List
from collections import defaultdict

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        hsh = defaultdict(list)
        for word in dictionary:
            hsh[word[0]] += [word]
        print(f'\thsh = {hsh}')
        # Refresh the hsh values
        for k in hsh:
            arr = [(len(i), i) for i in hsh[k]]
            arr = sorted(arr, key=lambda x: -x[0])
            val = [x[1] for x in arr]
            hsh[k] = val
        print(f'\thsh = {hsh}')
        res = ''
        while len(s) > 0:
        #if len(s) > 0:
            print(f'\ts = {s}')
            ch = s[0]
            if ch in hsh:
                found = False
                for v in hsh[ch]:
                    if s.find(v) == 0:
                        s = s.replace(v,'',1)
                        found = True
                        break
                if not found:
                    res += ch
                    s = s[1:]
            else:
                res += ch 
                s = s[1:]
        print(f'\tres, s = {res}, {s}')
        return len(res)

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


