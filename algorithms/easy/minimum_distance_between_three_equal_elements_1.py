from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        N = len(nums)
        MAX = 10**20
        res = MAX
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if nums[i] == nums[j] == nums[k]:
                        distance = abs(i - j) + abs(j - k) + abs(k - i)
                        res = min(res, distance)
        return -1 if res == MAX else res

# Main section
for nums in [
               [1,2,1,1,3],
               [1,1,2,3,2,1,2],
               [1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumDistance(nums)
    print(f'r = {r}')
    print('=====================')

