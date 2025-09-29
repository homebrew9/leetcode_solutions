from typing import List
from collections import defaultdict

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        # Iterative solution
        hsh = defaultdict(str)
        for k, v in replacements:
            hsh[f'%{k}%'] = v
        res = text
        while True:
            found = False
            for k in hsh:
                if k in res:
                    found = True
                    res = res.replace(k, hsh[k])
            if not found:
                break
        return res
    def applySubstitutions_1(self, replacements: List[List[str]], text: str) -> str:
        # Recursive solution
        def solve(s):
            i = s.find('%')
            if i >= 0:
                k = s[i:i+3]
                s = solve(s[:i] + hsh[k] + s[i+3:])
            return s
        hsh = defaultdict(str)
        for k, v in replacements:
            hsh[f'%{k}%'] = v
        res = solve(text)
        return res

# Main section
for replacements, text in [
                             ([['A','abc'],['B','def']], '%A%_%B%'),
                             ([['A','bce'],['B','ace'],['C','abc%B%']], '%A%_%B%_%C%'),
                             ([['O','zpnbuso'],['N','p%O%d%O%'],['D','%N%ju']], '%O%_%N%_%D%'),
                          ]:
    print(f'replacements = {replacements}')
    print(f'text = {text}')
    sol = Solution()
    r = sol.applySubstitutions(replacements, text)
    r1 = sol.applySubstitutions_1(replacements, text)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('=============================')

