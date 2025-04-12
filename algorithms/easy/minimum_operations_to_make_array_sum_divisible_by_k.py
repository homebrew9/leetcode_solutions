from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k

# Main section
for nums, k in [
                  ([3,9,7], 5),
                  ([4,1,3], 4),
                  ([3,2], 6),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.minOperations(nums, k)
    print(f'r = {r}')
    print('========================')

