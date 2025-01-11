from collections import defaultdict
from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        hsh = defaultdict(int)
        for i, n in enumerate(nums[:-1]):
            if n == key:
                hsh[nums[i+1]] += 1
        #print(f'\thsh = {hsh}')
        max_val = max(hsh.values())
        for k, v in hsh.items():
            if v == max_val:
                return k

# Main section
for nums, key in [
                   ([1,100,200,1,100], 1),
                   ([2,2,2,2,3], 2),
                   ([1,1], 1),
                ]:
    print(f'nums, key = {nums}, {key}')
    sol = Solution()
    r = sol.mostFrequent(nums, key)
    print(f'r = {r}')
    print('================')

