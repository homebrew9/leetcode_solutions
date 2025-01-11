from typing import List

class Solution:
    #def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #    for i, g in enumerate(gas):
    #        if g >= cost[i]:
    #            tank = 0
    #            for j in range(i, i+len(gas)):
    #                ind = j % len(gas)
    #                tank += gas[ind] - cost[ind]
    #                if tank < 0:
    #                    break
    #            if tank >= 0:
    #                return i
    #    return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        gas = gas + gas
        cost = cost + cost
        current = 0
        start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            current += g
            current -= c
            if current < 0:
                start = i + 1
                current = 0
            else:
                if i - start >= N:
                    return start
        return -1

# Main section
for gas, cost in [
                    ([1,2,3,4,5], [3,4,5,1,2]),
                    ([2,3,4], [3,4,3]),
                    ([20,4,16,0,14,2,17,13,20,8,1,12,8,3,6,8,14,6,13,3,8,16,4,9,1,16,6,8,6,5], [17,16,1,4,20,17,14,15,10,12,18,14,16,0,0,4,14,2,9,18,5,16,8,9,17,10,2,20,9,0]),
                    ([1,4,16,0,0,4,14,2,9,18,5,16,8,9,17,10,2,20,9,0], [4,0,2,17,8,1,8,3,6,8,6,3,8,4,9,1,6,8,6,5]),
                 ]:
    print(f'gas, cost = {gas}, {cost}')
    sol = Solution()
    r = sol.canCompleteCircuit(gas, cost)
    print(f'r = {r}')
    print('=================')



