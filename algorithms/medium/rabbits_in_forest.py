import math
from typing import List
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Intuition: Let's say answers = [3,3,3,3,3]. We first start with a batch B1 of 4 rabbits. The first 4 rabbits
        # who said "3" are all from batch B1. The fifth rabbit in "answers" (index=4) cannot be from batch B1. It must
        # be from batch B2 of 4 rabbits again! In fact, rabbits at indices 4,5,6,7 (if there were any) would be from
        # batch B2, and so on. So for each frequency, we find the quotient of frequency / (key + 1). In this case, we
        # have q = 5 / 4 = 1.25 and ceiling of q = 2. So we have 4 * 2 = 8 rabbits minimum.
        cntr = Counter(answers)
        res = 0
        for k, v in cntr.items():
            q = math.ceil(v / (k + 1))
            res += q * (k + 1)
        return res

# Main section
for answers in [
                  [1,1,2],
                  [10,10,10],
                  [0,0,0],
                  [94,84,43,61,78,32,92,8,82,78,50,26,54,68,50,18,58,94,33,13,90,66,100,92,43,0,26,65,22,61,40,41,71,86,53,21,40,52,30,16],
               ]:
    print(f'answers = {answers}')
    sol = Solution()
    r = sol.numRabbits(answers)
    print(f'r = {r}')
    print('========================')

