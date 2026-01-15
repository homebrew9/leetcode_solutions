from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_consecutive_length(nums):
            N = len(nums)
            nums.sort()
            res = -10**20
            curr = 0
            for i in range(0, N):
                if i == 0 or nums[i] != nums[i-1] + 1:
                    curr = 1
                elif nums[i] == nums[i-1] + 1:
                    curr += 1
                res = max(res, curr)
            return res
        hb_max_consecutive = max_consecutive_length(hBars)
        vb_max_consecutive = max_consecutive_length(vBars)
        min_consecutive = min(hb_max_consecutive, vb_max_consecutive)
        max_square = (min_consecutive + 1) * (min_consecutive + 1)
        return max_square

# Main section
for n, m, hBars, vBars in [
                             (2, 1, [2,3], [2]),
                             (1, 1, [2], [2]),
                             (2, 3, [2,3], [2,4]),
                          ]:
    print(f'n, m, hBars, vBars = {n}, {m}, {hBars}, {vBars}')
    sol = Solution()
    r = sol.maximizeSquareHoleArea(n, m, hBars, vBars)
    print(f'r = {r}')
    print('==========================')









