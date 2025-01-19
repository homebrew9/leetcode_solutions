#
# TC = O(N^2) ; SC = O(N)
#
from collections import defaultdict
class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)
        hsh = defaultdict(int)
        for i in range(N):
            for j in range(i, N):
                hsh[s[i:j+1]] += 1
        res = -1
        for k, v in hsh.items():
            if len(set(k)) == 1 and v >= 3:
                res = max(res, len(k))
        return res

# Main section
for s in [
            'aaaa',
            'abcdef',
            'abcaba',
            'thlhjmtrxhycuicjnfpbjrviaydjuboptumxbmqqbjkpivdsqq',
            'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
            'aaaaaaaabbbbbbbbbccccccccccddddddddddddddddddddddd',
            'cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde',
            'eccdnmcnkl',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.maximumLength(s)
    print(f'r = {r}')
    print('====================')


