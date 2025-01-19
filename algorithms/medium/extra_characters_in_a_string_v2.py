#
# ===============================================================
# Not sure why the following definition of TrieNode creates the trie incorrectly!!
# class TrieNode:
#     def __init__(self, hsh=defaultdict(), end=False):
#         self.hsh = hsh
#         self.end = end
# ===============================================================
#
from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.hsh = defaultdict()
        self.end = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def createTrie(dictionary):
            root = TrieNode()
            for word in dictionary:
                curr = root
                for ch in word:
                    if ch not in curr.hsh:
                        curr.hsh[ch] = TrieNode()
                    curr = curr.hsh[ch]
                curr.end = True
            return root
        def solve(i):
            if i >= N:
                return 0
            if i in memo:
                return memo[i]
            # Either skip the current char and call the function recursively on the next character
            # Or, iterate till end of string and call the function right after a match
            res = 1 + solve(i + 1)
            curr = self.root
            for j in range(i, N):
                if s[j] not in curr.hsh:
                    break
                curr = curr.hsh[s[j]]
                if curr.end:
                    res = min(res, solve(j+1))
            memo[i] = res
            return memo[i]
        self.root = createTrie(dictionary)
        print(self.root.hsh.keys())
        memo = dict()
        N = len(s)
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
                        ('abcde', ['bcd','bc', 'cde']),
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


