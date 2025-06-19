from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = list()
        for i in range(0, N - 3 + 1, 3):
            if nums[i+2] - nums[i] > k:
                return []
            res += [nums[i:i+3]]
        return res

# Main section
for nums, k in [
                  ([1,3,4,8,7,9,3,5,1], 2),
                  ([2,4,2,2,5,2], 2),
                  ([4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 14),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.divideArray(nums, k)
    print(f'r = {r}')
    print('===========================')

















