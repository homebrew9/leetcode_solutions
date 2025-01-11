from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = None
        for i, n in enumerate(nums):
            if n == 1:
                if prev is None or (i - prev) > k:
                    prev = i
                else:
                    return False
        return True

# Main section
for nums, k in [
                  ([1,0,0,0,1,0,0,1], 2),
                  ([1,0,0,1,0,1], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.kLengthApart(nums, k)
    print(f'r = {r}')
    print('===================')

