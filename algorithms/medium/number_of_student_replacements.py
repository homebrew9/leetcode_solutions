from typing import List

class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        N = len(ranks)
        res = 0
        best = ranks[0]
        for i in range(1, N):
            if ranks[i] < best:
                res += 1
                best = ranks[i]
        return res

# Main section
for ranks in [
                [4,1,2],
                [2,2,3],
                [26,55,32,36,15,88,39,31,18,14,30,65,24,78,54,100,69,47,74,45,29,22,54,90,70,23,95,27,48,87,72,82,2,7,23,27,9,73,87,53],
             ]:
    print(f'ranks = {ranks}')
    sol = Solution()
    r = sol.totalReplacements(ranks)
    print(f'r = {r}')
    print('============================')








