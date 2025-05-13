from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return '111' in ''.join(str(n%2) for n in arr)

# Main section
for arr in [
              [2,6,4,1],
              [1,2,34,3,4,5,7,23,12],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.threeConsecutiveOdds(arr)
    print(f'r = {r}')
    print('============================')

