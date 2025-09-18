from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        num_set = set(nums)
        start_val = max(1, int(avg) + 1)
        for n in range(start_val, 102):
            if n not in num_set:
                return n

# Main section
for nums in [
               [3,5],
               [-1,1,2],
               [4,-1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.smallestAbsent(nums)
    print(f'r = {r}')
    print('===================')



























