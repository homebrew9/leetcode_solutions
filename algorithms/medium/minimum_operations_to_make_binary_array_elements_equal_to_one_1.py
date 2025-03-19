from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        flips = [0 for _ in range(N)]
        i = 0
        res = 0
        while i < N:
            while i < N and (nums[i] + flips[i]) % 2 == 1:
                i += 1
            if N - i < 3:
                break
            for j in range(3):
                flips[i+j] += 1
            res += 1
        return -1 if i < N else res

# Main section
for nums in [
               [0,1,1,1,0,0],
               [0,1,1,1],
               [0,0,0,0,0,0,0,0,0],
               [1,1,1,1,1,1,1,1,1],
               [1,0,0,0,1,0,0,0,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minOperations(nums)
    print(f'r  = {r}')
    print('================')

