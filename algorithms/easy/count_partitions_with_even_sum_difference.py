from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        N = len(nums)
        total = sum(nums)
        left_sum = 0
        right_sum = 0
        res = 0
        for i in range(N-1):
            left_sum += nums[i]
            right_sum = total - left_sum
            if abs(left_sum - right_sum) % 2 == 0:
                res += 1
        return res

# Main section
for nums in [
               [10,10,3,7,6],
               [1,2,2],
               [2,4,6,8],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.countPartitions(nums)
    print(f'r = {r}')
    print('==================')


