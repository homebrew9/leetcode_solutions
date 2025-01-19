from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = list()
        curr = folder[0]
        for i in range(1, len(folder)):
            v = folder[i]
            if v.find(curr + '/') != 0:
                res.append(curr)
                curr = v
        if curr:
            res.append(curr)
        return res

# Main section
for folder in [
                 ['/a','/a/b','/c/d','/c/d/e','/c/f'],
                 ['/a','/a/b/c','/a/b/d'],
                 ['/a/b/c','/a/b/ca','/a/b/d'],
                 ['/a/b/c','/a/b/ca/pq/xy/df','/a/b/d/e/m/n/r/s/t'],
                 ['/a','/b','/c','/a/b/'],
              ]:
    print(f'folder = {folder}')
    sol = Solution()
    r = sol.removeSubfolders(folder)
    print(f'r = {r}')
    print('==================')


