from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 10**20
        for i in range(k-1, len(nums)):
            diff = nums[i] - nums[i-k+1]
            res = min(res, diff)
        return res
    def minimumDifference_1(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min([nums[i] - nums[i-k+1] for i in range(k-1, len(nums))])

# Main section
for nums, k in [
                  ([90], 1),
                  ([9,4,1,7], 2),
                  ([27,20,7,74,53,23,22,83,40,44,98,38,90,61,12,7,63,5,10,23,31,0,56,57,12,5,2,39,51,49,26,38,6,59,98,65,44,7,71,78,65,27,79,61,17,86,90,20,5,8], 13),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.minimumDifference(nums, k)
    r1 = sol.minimumDifference_1(nums, k)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('==========================')















