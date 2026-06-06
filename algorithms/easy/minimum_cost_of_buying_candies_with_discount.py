from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        total_cost = 0
        buy = 0
        for i in range(len(cost)-1, -1, -1):
            if buy < 2:
                buy += 1
                total_cost += cost[i]
            else:
                buy = 0
        return total_cost

# Main section
for cost in [
               [1,2,3],
               [6,5,7,9,2,2],
               [5,5],
            ]:
    print(f'cost = {cost}')
    sol = Solution()
    r = sol.minimumCost(cost)
    print(f'r = {r}')
    print('==============================')









