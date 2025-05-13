from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        N = len(arr)
        for i in range(0, N-2):
            if arr[i] % 2 == arr[i+1] % 2 == arr[i+2] % 2 == 1:
                return True
        return False

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


