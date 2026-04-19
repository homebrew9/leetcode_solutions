class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)
        lpfx = [-1 for _ in range(N)]
        for i in range(N):
            lpfx[i] = nums[i] if i == 0 else max(lpfx[i-1], nums[i])
        rpfx = [-1 for _ in range(N)]
        for i in range(N-1, -1, -1):
            rpfx[i] = nums[i] if i == N-1 else min(nums[i], rpfx[i+1])
        for i in range(N):
            if lpfx[i] - rpfx[i] <= k:
                return i
        return -1

# Main section
for nums, k in [
                  ([5,0,1,4], 3),
                  ([3,2,1], 1),
                  ([0], 0),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.firstStableIndex(nums, k)
    print(f'r = {r}')
    print('==================================')












