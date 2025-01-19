from typing import List
from collections import defaultdict

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        hpref = defaultdict(list)
        for i in range(len(preferences)):
            hpref[i] = preferences[i]
        hpair = defaultdict(int)
        for x, y in pairs:
            hpair[x] = y
            hpair[y] = x
        def get_pref_over(x, y):
            # Given a person x, return a list of all persons that
            # x prefers over y
            res = list()
            for f in hpref[x]:
                if f != y:
                    res.append(f)
                else:
                    break
            return res
        res = 0
        for k, v in hpair.items():
            lst = get_pref_over(k, v)
            for item in lst:
                paired_with = hpair[item]
                arr = get_pref_over(item, paired_with)
                if k in arr:
                    res += 1
                    break
        return res

# Main section
for n, preferences, pairs in [
                                (4, [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], [[0,1],[2,3]]),
                                (2, [[1],[0]], [[1,0]]),
                                (4, [[1,3,2],[2,3,0],[1,3,0],[0,2,1]], [[1,3],[0,2]]),
                                (4, [[1,3,2],[2,3,0],[1,0,3],[1,0,2]], [[2,1],[3,0]]),
                             ]:
    print(f'n, preferences, pairs = {n}, {preferences}, {pairs}')
    sol = Solution()
    r = sol.unhappyFriends(n, preferences, pairs)
    print(f'r = {r}')
    print('==========================')


