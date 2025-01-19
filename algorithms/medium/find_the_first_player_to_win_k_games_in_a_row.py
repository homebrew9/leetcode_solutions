from typing import List
from collections import defaultdict

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        N = len(skills)
        hsh = defaultdict(int)
        i, j = 0, 1
        while i < N and j < N and i != j:
            print(i, j, hsh)
            if skills[i] > skills[j]:
                hsh[i] += 1
                if hsh[i] >= k:
                    return i
                hsh[j] = 0
                j = max(i, j) + 1
                #next_j = (max(i, j) + 1) % N
                #if next_j == j:
                #    j += 1
                #else:
                #    j = next_j
            else:
                hsh[j] += 1
                if hsh[j] >= k:
                    return j
                hsh[i] = 0
                i = max(i, j) + 1
                #next_i = (max(i, j) + 1) % N
                #if next_i == i:
                #    i += 1
                #else:
                #    i = next_i
            #if i >= N:
            #    i = 0
            #if j >= N:
            #    j = 0
        return i - 1
            
# Main section
for skills, k in [
                    ([4,2,6,3,9], 2),
                    ([2,5,4], 3),
                    ([16,4,7,17], 562084119),
                    ([11,9,12,2,20,1,8], 3),
                 ]:
    print(f'skills, k = {skills}, {k}')
    sol = Solution()
    r = sol.findWinningPlayer(skills, k)
    print(f'r = {r}')
    print('======================')


