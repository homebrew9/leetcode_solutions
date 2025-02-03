from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        # Intuition: There should be at the most one "drop"
        N = len(nums)
        if N == 1:
            return True
        drop_count = 0
        for i in range(1, N+1):
            prev = i - 1
            curr = i % N
            if nums[curr] < nums[prev]:
                drop_count += 1
        return drop_count <= 1

# Main section
for nums in [
               [3,4,5,1,2],
               [2,1,3,4],
               [1,2,3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.check(nums)
    print(f'r = {r}')
    print('========================')

