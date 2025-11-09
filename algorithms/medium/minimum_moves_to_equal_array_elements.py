from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total = sum(nums)
        min_val = min(nums)
        N = len(nums)
        return total - min_val * N

# Main section
for nums in [
               [1,2,3],
               [1,1,1],
               [30,26,3,20,25,23,11,11,23,26],
               [-55,-13,57,-84,-54,-33,62,-45,88,-65,-36,29,-27,34,96,40,55,-80,51,62,9,49,64,37,37,-92,36,81,24,70,-8,37,-77,-51,-60,10,-32,78,-43,30],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minMoves(nums)
    print(f'r = {r}')
    print('=====================')



