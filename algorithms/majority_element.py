from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        majority = len(nums) // 2
        hsh = dict()
        for num in nums:
            if num in hsh:
                hsh[num] += 1
                if hsh[num] > majority:
                    return num
            else:
                hsh[num] = 1

# Main section
sol = Solution()
for nums in [
                 [3,2,3],
                 [2,2,1,1,1,2,2],
                 [1],
                 [2,2],
                 [1,2,1],
            ]:
    print(f'nums = {nums}')
    r = sol.majorityElement(nums)
    print(f'r    = {r}')
    print('===============================')

