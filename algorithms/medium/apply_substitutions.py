from typing import List
from collections import defaultdict, deque

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
    def applySubstitutions_2(self, replacements: List[List[str]], text: str) -> str:
        # Topological sort
        hsh = defaultdict(str)
        hsh1 = defaultdict(set)
        for k, v in replacements:
            key = f'%{k}%'
            hsh[key] = v
            hsh1[key] = set()
            N = len(v)
            i = 0
            while i < N:
                if v[i] == '%':
                    hsh1[key].add(v[i:i+3])
                    i += 3
                    continue
                i += 1
        # We use Kahn's algorithm for Topological Sorting.
        dq = deque()
        key_list = list(hsh1.keys())
        for k in key_list:
            if len(hsh1[k]) == 0:
                dq.append(k)
                del hsh1[k]
        while dq:
            key = dq.popleft()
            key_list = list(hsh1.keys())
            for k in key_list:
                if key in hsh1[k]:
                    hsh[k] = hsh[k].replace(key, hsh[key])
                    hsh1[k].remove(key)
                    if len(hsh1[k]) == 0:
                        dq.append(k)
                        del hsh1[k]
        return '_'.join([hsh[k] for k in text.split('_')])

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
    r2 = sol.applySubstitutions_2(replacements, text)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    assert(r == r1 == r2)
    print('=============================')





