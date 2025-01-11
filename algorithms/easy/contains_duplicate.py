from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cntr = Counter(nums)
        # If all elements are distinct, their values will be 1
        # In that case, sum of values array = len of values array
        if sum(cntr.values()) == len(cntr.values()):
            return False
        return True

# Main section
for nums in [
               [1,2,3,1],
               [1,4,2,3],
               [9,2,9,46],
               [9,2,7,6],
               [1,1,1,3,3,4,3,2,4,2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.containsDuplicate(nums)
    print(f'r = {r}')
    print('===========================')

