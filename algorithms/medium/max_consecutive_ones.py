from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        pfx_left = nums[:]
        for i in range(N):
            if pfx_left[i] == 1:
                if i > 0 and pfx_left[i-1] > 0:
                    pfx_left[i] = pfx_left[i-1] + 1
                res = max(res, pfx_left[i])
        pfx_right = nums[:]
        for i in range(N-1, -1, -1):
            if pfx_right[i] == 1:
                if i < N - 1 and pfx_right[i+1] > 0:
                    pfx_right[i] = pfx_right[i+1] + 1
                res = max(res, pfx_right[i])
        for i in range(N):
            if nums[i] == 0:
                val = 0
                if i == 0:
                    if i + 1 < N:
                        val = pfx_right[i+1]
                elif i == N - 1:
                    if i - 1 >= 0:
                        val = pfx_left[i-1]
                else:
                    val = pfx_left[i-1] + pfx_right[i+1]
                res = max(res, val + 1)
        return res

# Main section
for nums in [
                 [1,0,1,1,0],
                 [1,0,1,1,0,1],
                 [0,1,1,1,0],
                 [1,0,0,0,1],
                 [0,0,0],
                 [1,1,1,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findMaxConsecutiveOnes(nums)
    print(f'r = {r}')
    print('===================')

