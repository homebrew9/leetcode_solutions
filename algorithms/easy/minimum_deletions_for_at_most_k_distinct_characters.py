from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        cntr = Counter(s)
        arr = sorted([(k, v) for k, v in cntr.items()], key=lambda x: (-x[1], x[0]))
        return sum([x[1] for x in arr[k:]])

# Main section
for s, k in [
               ('abc', 2),
               ('aabb', 2),
               ('yyyzz', 1),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.minDeletion(s, k)
    print(f'r = {r}')
    print('============================')



















