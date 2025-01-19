from typing import List
from sortedcontainers import SortedList

class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        # The ratio of price to weight is the most important. We want to
        # collect the greatest price per weight at each step. Hence we
        # use p/w in our SortedList.
        arr = [[p/w, p, w] for p, w in items]
        sl = SortedList(arr)
        res = 0
        N = len(sl)
        for i in range(N-1, -1, -1):
            _, p, w = sl[i]
            if capacity >= w:
                capacity -= w
                res += p
                if capacity == 0:
                    return res
            else:
                res += p * capacity / w
                return res
        return -1

# Main section
for items, capacity in [
                          ([[50,1],[10,8]], 5),
                          ([[100,30]], 50),
                          ([[100,15],[90,10],[80,10],[70,10],[60,7],[50,6]], 50),
                          ([[41,52],[18,67],[22,24],[48,39],[40,59],[47,91],[65,2],[16,68],[78,38],[73,23],[45,42],[43,71],[68,98],[66,17],[72,46],[87,45],[63,9],[74,78],[63,44],[31,36],[72,23],[59,40],[24,27],[11,13],[68,68],[15,7],[42,68],[80,91],[40,65],[38,13],[9,96],[93,36],[24,70],[57,6],[62,60],[37,12],[38,34],[37,54],[32,68],[58,77],[58,4],[71,76],[52,44],[56,58],[61,2],[3,36],[27,14],[55,70],[61,55],[5,97],[15,88],[72,20],[71,56],[27,70],[14,65],[80,82],[52,87],[92,86],[48,49],[58,92],[2,55],[95,47],[9,44],[16,93],[76,1],[34,92],[38,28],[33,8],[66,72],[59,49]], 250),
                       ]:
    print(f'items, capacity = {items}, {capacity}')
    sol = Solution()
    r = sol.maxPrice(items, capacity)
    print(f'r = {r}')
    print('====================')


