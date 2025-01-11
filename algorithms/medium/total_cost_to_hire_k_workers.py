from sortedcontainers import SortedList
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        sl_left, sl_right = SortedList(), SortedList()
        left, right = 0, N - 1
        while left < candidates:
            sl_left.add(costs[left])
            left += 1
        while right > left and right >= N - candidates:
            sl_right.add(costs[right])
            right -= 1
        print(f'\tsl_left, sl_right = {sl_left}, {sl_right}')
        print(f'\tleft, right = {left}, {right}')
        res = 0
        while k > 0:
            print(f'\tk, res = {k}, {res}')
            print(f'\tsl_left, sl_right = {sl_left}, {sl_right}')
            print(f'\tleft, right = {left}, {right}')
            if len(sl_left) > 0 and len(sl_right) > 0:
                if sl_left[0] <= sl_right[0]:
                    res += sl_left.pop(0)
                    if left <= right:
                        sl_left.add(costs[left])
                        left += 1
                elif sl_right[0] < sl_left[0]:
                    res += sl_right.pop(0)
                    if left <= right:
                        sl_right.add(costs[right])
                        right -= 1
            elif len(sl_left) > 0:
                res += sl_left.pop(0)
                if left <= right:
                    sl_left.add(costs[left])
                    left += 1
            else:
                res += sl_right.pop(0)
                if left <= right:
                    sl_right.add(costs[right])
                    right -= 1
            k -= 1
            print('=====')
        return res

# Main section
for costs,k,candidates in [
                             ([17,12,10,2,7,2,11,20,8], 3, 4),
                             ([1,2,4,1], 3, 3),
                             ([1,2,3], 3, 3),
                             ([9,8,7,6,5,4,3,2,1], 4, 2),
                             ([9,8,7,6,5,4,3,2,1], 7, 2),
                             ([1,2,3,4,5,6,7,8,9], 7, 2),
                             ([1,2,3,4,5,6,7,8,9], 1, 1),
                             ([9,8,7,6,5,4,3,2,1], 1, 1),
                             ([1,2,3,9,9,9,1,2,3], 8, 3),
                             ([57,33,26,76,14,67,24,90,72,37,30], 11, 2),
                          ]:
    print(f'costs, k, candidates = {costs}, {k}, {candidates}')
    sol = Solution()
    r = sol.totalCost(costs, k, candidates)
    print(f'r = {r}')
    print('==================')


