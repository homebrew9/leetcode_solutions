# ==================================================================
# For 1st testcase : I can't figure this out!!! Why is the minimum value 1 ??????
#     grid = [[0, 1], [0, 1], [0, 0]]
#     self.res_rows = 2
#     self.res_cols = 100000000000000000000
#     min(self.res_rows, self.res_cols) = 1
#     r = 1
# ==================================================================

from typing import List
import itertools

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def flips_needed(arr):
            N = len(arr)
            total_ones = arr.count(1)
            total_zeros = N - total_ones
            diff = 0
            i, j = 0, N-1
            while i < j:
                if arr[i] != arr[j]:
                    diff += 1
                i += 1
                j -= 1
            change_set = set()
            for item in itertools.product(*[[-1,1] for d in range(diff)]):
                change_set.add((diff, total_ones + sum(item)))
            # All zeros
            change_set.add((total_ones, 0))
            # All ones
            change_set.add((total_zeros, N))
            return list(change_set)
        def solve(r, flips_so_far, one_count_so_far):
            #print(r, flips_so_far, one_count_so_far)
            if r >= rows:
                if one_count_so_far % 4 == 0:
                    #self.res_rows = min(self.res_rows, flips_so_far)
                    self.res = min(self.res, flips_so_far)
                return
            for f, oc in flips_needed(grid[r]):
                total_flips = flips_so_far + f
                total_oc = one_count_so_far + oc
                solve(r+1, total_flips, total_oc)
        def solve1(c, flips_so_far, one_count_so_far):
            #print(c, flips_so_far, one_count_so_far)
            if c >= cols:
                if one_count_so_far % 4 == 0:
                    #self.res_cols = min(self.res_cols, flips_so_far)
                    self.res = min(self.res, flips_so_far)
                return
            for f, oc in flips_needed(col_arr[c]):
                total_flips = flips_so_far + f
                total_oc = one_count_so_far + oc
                solve(c+1, total_flips, total_oc)

        #self.res_rows = 10**20
        #self.res_cols = 10**20
        self.res = 10**20
        rows = len(grid)
        cols = len(grid[0])
        solve(0, 0, 0)
        #print(f'self.res_rows = {self.res_rows}')
        col_arr = list()
        for c in range(cols):
            tmp = list()
            for r in range(rows):
                tmp += [grid[r][c]]
            col_arr += [tmp]
        #print(col_arr)
        solve1(0, 0, 0)
        #print(f'self.res_cols = {self.res_cols}')
        #print(f'min(self.res_rows, self.res_cols) = {min(self.res_rows, self.res_cols)}')
        #return min(self.res_rows, self.res_cols)
        #return min(2, self.res_cols)
        return self.res

# Main section
for grid in [
               [[0,1],[0,1],[0,0]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.minFlips(grid)
    print(f'r = {r}')
    print('==================')

