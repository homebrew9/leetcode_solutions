from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        duplicate, missing = None, None
        for i in range(N):
            if i == 0:
                if nums[i] != 1:
                    missing = 1
                continue
            if nums[i] == nums[i-1]:
                duplicate = nums[i]
            if nums[i] == nums[i-1] + 2:
                missing = nums[i] - 1
            if duplicate is not None and missing is not None:
                break
        if missing is None:
            missing = N
        return [duplicate, missing] # type: ignore

    def findErrorNums_1(self, nums: List[int]) -> List[int]:
        N = len(nums)
        missing = list(set(range(1, N+1)) - set(nums))[0]
        duplicate = None
        cntr = Counter(nums)
        for k, v in cntr.items():
            if v == 2:
                duplicate = k
                break
        return [duplicate, missing] # type: ignore

# Main section
for nums in [
               [1,2,2,4],
               [1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findErrorNums(nums)
    r1 = sol.findErrorNums_1(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('===========================')






































