from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # Let Alice give x candies to Bob.
        # Let Bob give y candies to Alice. Then,
        # sa - x + y = sb - y + x
        # => 2(y - x) = (sb - sa)
        # => y = x + (sb - sa)/2
        # For each candy x that Alice has, check if Bob has y = x + (sb - sa)/2 candies
        sa = sum(aliceSizes)
        sb = sum(bobSizes)
        setb = set(bobSizes)
        for x in aliceSizes:
            if x + (sb - sa)//2 in setb:
                return [x, x + (sb - sa)//2]

# Main section
for aliceSizes, bobSizes in [
                               ([1,1], [2,2]),
                               ([1,2], [2,3]),
                               ([2], [1,3]),
                               ([1,2,3,4,5], [7,8,5,3,2]),
                               ([1,2,3,4,5], [3,6,2]),
                               ([1,2,3,4,5], [1,4,2,3,5,3,2,1]),
                            ]:
    print(f'aliceSizes, bobSizes = {aliceSizes}, {bobSizes}')
    sol = Solution()
    r = sol.fairCandySwap(aliceSizes, bobSizes)
    print(f'r = {r}')
    print('=============================')

