from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # TC = O(N), SC = O(N)
        unmatched = set()
        for n in nums:
            if n in unmatched:
                unmatched.remove(n)
            else:
                unmatched.add(n)
        # There should be no unmatched integer in the end
        return len(unmatched) == 0

    def divideArray_1(self, nums: List[int]) -> bool:
        # TC = O(N), SC = O(N)
        cntr = Counter(nums)
        for v in cntr.values():
            if v % 2 == 1:
                return False
        return True

    def divideArray_2(self, nums: List[int]) -> bool:
        # TC = O(NLogN), SC = O(1)
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i+1]:
                return False
        return True

# Main section
for nums in [
               [3,2,3,2,2,2],
               [1,2,3,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.divideArray(nums)
    r1 = sol.divideArray_1(nums)
    r2 = sol.divideArray_2(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('================')

