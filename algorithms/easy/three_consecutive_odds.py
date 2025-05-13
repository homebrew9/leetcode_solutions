from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        for n in arr:
            if n % 2 == 1:
                odd_count += 1
                if odd_count == 3:
                    return True
            else:
                odd_count = 0
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




