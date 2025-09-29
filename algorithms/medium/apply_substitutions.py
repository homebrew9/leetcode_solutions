from typing import List
from collections import defaultdict

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
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
    print(f'r  = {r}')
    print('=============================')









