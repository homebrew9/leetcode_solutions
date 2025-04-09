from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        nums_set = set(nums)
        res = 0
        for n in nums_set:
            if n > k:
                res += 1
        return res
    def minOperations_1(self, nums: List[int], k: int) -> int:
        return -1 if k > min(nums) else len(list(filter(lambda x: x > k, set(nums))))

# Main section
for nums, k in [
                  ([5,2,5,4,5], 2),
                  ([2,1,2], 2),
                  ([9,7,5,3], 1),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.minOperations(nums, k)
    r1 = sol.minOperations_1(nums, k)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('========================')

