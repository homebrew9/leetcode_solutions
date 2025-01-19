#
# Wrong logic! Does not return the *minimum* moves!
# The answer for the last testcase (3rd one) is 1 but this algorithm returns 3.
#

from typing import List

class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        def move_count(nums):
            # Minimum number of moves to "even out" an array so that each
            # element equals 1.
            N = len(nums)
            steps = 0
            p1 = 0
            #while p1 < N and nums[p1] > 0:
            #    p1 += 1
            p2 = 0
            #while p2 < N and nums[p2] <= 1:
            #    p2 += 1
            #print(f'\tp1, p2 = {p1}, {p2}')
            while p1 < N:
                if nums[p1] > 0:
                    p1 += 1
                elif nums[p2] <= 1:
                    p2 += 1
                elif nums[p2] > 1:
                    steps += abs(p1 - p2)
                    nums[p1] += 1
                    nums[p2] -= 1
            return steps
        N = len(rooks)
        rows = [0 for _ in range(N)]
        cols = [0 for _ in range(N)]
        for r, c in rooks:
            rows[r] += 1
            cols[c] += 1
        return move_count(rows) + move_count(cols)

# Main section
for rooks in [
                [[0,0],[1,0],[1,1]],
                [[0,0],[0,1],[0,2],[0,3]],
                [[0,1],[1,2],[2,1],[3,3]],
                [[0,1],[3,2],[1,4],[0,2],[3,4]],
             ]:
    print(f'rooks = {rooks}')
    sol = Solution()
    r = sol.minMoves(rooks)
    print(f'r = {r}')
    print('====================')


