from typing import List

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        return sorted(set(nums), reverse=True)[:k]

# Main section
for nums, k in [
                  ([84,93,100,77,90], 3),
                  ([84,93,100,77,93], 3),
                  ([1,1,1,2,2,2], 6),
               ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxKDistinct(nums, k)
    print(f'r = {r}')
    print('===================')


