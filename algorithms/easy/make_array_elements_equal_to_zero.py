from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        N = len(nums)
        pfx_left = [0 for _ in range(N)]
        for i in range(N):
            pfx_left[i] = nums[i] if i == 0 else pfx_left[i-1] + nums[i]
        pfx_right = [0 for _ in range(N)]
        for i in range(N-1, -1, -1):
            pfx_right[i] = nums[i] if i == N - 1 else pfx_right[i+1] + nums[i]
        res = 0
        for i, v in enumerate(nums):
            if v == 0:
                # If left_sum = right_sum, then ping-pong on both sides will make the array all-zeros.
                # If left_sum = right_sum + 1, then ping-pong starting with *left* will result in all-zeros.
                # If right_sum = left_sum + 1, then ping-pong starting with *right* will result in all-zeros.
                if pfx_left[i] == pfx_right[i]:
                    res += 2
                if pfx_left[i] == pfx_right[i] + 1:
                    res += 1
                if pfx_right[i] == pfx_left[i] + 1:
                    res += 1
        return res

# Main section
for nums in [
               [1,0,2,0,3],
               [2,3,4,0,4,1,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.countValidSelections(nums)
    print(f'r = {r}')
    print('=====================')






