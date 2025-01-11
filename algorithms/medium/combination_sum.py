#
# This seems to take some time and might TLE. However, it might work since as per the problem description:
# "The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input."
#
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combine(num, res):
            #print(f'\tnum, res = {num}, {res}')
            if num >= target:
                if num == target:
                    self.st.add(tuple(sorted(res)))
                return
            for i in candidates:
                if num + i <= target:
                    combine(num+i, res+[i])

        res = list()
        num = 0
        self.st = set()
        for i in candidates:
            if num + i <= target:
                combine(num+i, res+[i])
        res = []
        for i in self.st:
            res.append(list(i))
        return res

# Main section
for candidates, target in [
                             ([2,3,6,7], 7),
                             ([2,3,5], 8),
                             ([2], 1),
                             ([2,3,4,5], 10),
                             ([2,4,6,7,9,11,12,14,16,17], 40),
                             #([2,4,6,7,9,11,12,14,16,17,18,21,23,26,27,29,30,31,33,35], 40),
                          ]:
    print(f'candidates, target = {candidates}, {target}')
    sol = Solution()
    r = sol.combinationSum(candidates, target)
    print(f'r = {r}')
    print('================')

