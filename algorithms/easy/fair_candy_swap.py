#
# Doesn't work!! The formula is incorrect. Logic is wrong.
# Study the problem and solution carefully!!
#
from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        arr = []
        equal_amount = abs(sum(aliceSizes) - sum(bobSizes))//2
        #print(f'\tequal_amount = {equal_amount}')
        for amt in aliceSizes:
            if amt - equal_amount in bobSizes:
                arr = [amt, equal_amount-amt]
                return arr
        for amt in bobSizes:
            if amt - equal_amount in aliceSizes:
                arr = [amt-equal_amount, amt]
                return arr

# Main section
for aliceSizes, bobSizes in [
                               ([1,1], [2,2]),
                               ([1,2], [2,3]),
                               ([2], [1,3]),
                            ]:
    print(f'aliceSizes, bobSizes = {aliceSizes}, {bobSizes}')
    sol = Solution()
    r = sol.fairCandySwap(aliceSizes, bobSizes)
    print(f'r = {r}')
    print('=============================')

