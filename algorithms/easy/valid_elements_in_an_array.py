class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        N = len(nums)
        lpfx = [-1 for _ in range(N)]
        for i in range(N):
            lpfx[i] = nums[i] if i == 0 else max(lpfx[i-1], nums[i])
        rpfx = [-1 for _ in range(N)]
        for i in range(N-1, -1, -1):
            rpfx[i] = nums[i] if i == N-1 else max(rpfx[i+1], nums[i])
        res = list()
        for i in range(N):
            if i == 0 or i == N-1 or nums[i] > lpfx[i-1] or nums[i] > rpfx[i+1]:
                res.append(nums[i])
        return res

# Main section
for nums in [
               [1,2,4,2,3,2],
               [5,5,5,5],
               [1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findValidElements(nums)
    print(f'r = {r}')
    print('==================================')






