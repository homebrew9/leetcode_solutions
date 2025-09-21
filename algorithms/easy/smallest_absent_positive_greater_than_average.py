from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        num_set = set(nums)
        n = max(1, int(avg) + 1)
        while n <= 101:
            if n not in num_set:
                break
            n += 1
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

