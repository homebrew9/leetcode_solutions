from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        max_val = max(target)
        target_set = set(target)
        res = list()
        i = 1
        while i <= max_val:
            res.append('Push')
            if i not in target_set:
                res.append('Pop')
            i += 1
        return res

# Main section
for target, n in [
                    ([1,3], 3),
                    ([1,2,3], 3),
                    ([1,2], 4),
                 ]:
    print(f'target, n = {target}, {n}')
    sol = Solution()
    r = sol.buildArray(target, n)
    print(f'r = {r}')
    print('===========================')












