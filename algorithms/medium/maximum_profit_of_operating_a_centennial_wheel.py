from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        N = len(customers)
        arr = list()
        i = 0
        carry_over = 0
        turns = 0
        while i < N:
            num = customers[i] + carry_over
            q, r = divmod(num, 4)
            if q == 0 and r >= 0:
                arr += [r]
                carry_over = 0
                turns += 1
            else:
                arr += [4] * q
                carry_over = r
                turns += q
            if turns >= N:
                carry_over = 0
                break
            i += 1
        if carry_over > 0:
            arr += [carry_over]
        #print(arr)
        res = sum(arr) * boardingCost - len(arr) * runningCost
        return -1 if res <= 0 else len(arr)
            
# Main section
for customers, boardingCost, runningCost in [
        ([8,3], 5, 6),
        ([10,9,6], 6, 4),
        ([3,4,0,5,1], 1, 92),
        ([1,1,1,1,1,1,1,1,1,1,1], 1, 1),
        ([1,9,3,0,10,4,4,7,0,3,10,6,5,5,2,9,6,0,5,4], 2, 3),
        ([4,7,0,3,10,6,5,5,2,9], 2, 3),
        ([5,4], 2, 3),
    ]:
    print(f'customers    = {customers}')
    print(f'boardingCost = {boardingCost}')
    print(f'runningCost  = {runningCost}')
    sol = Solution()
    r = sol.minOperationsMaxProfit(customers, boardingCost, runningCost)
    print(f'r = {r}')
    print('=========================')




