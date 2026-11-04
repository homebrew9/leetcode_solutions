class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(1, N-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                res += nums[i]
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                res -= nums[i]
        return res

# Main section
for nums in [
               [1,5,2,4,1,3,0],
               [-5,-6,-1,-2,5,3,2],
               [6,5,2,5,5,3,6],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.peakValleyDifference(nums)
    print(f'r = {r}')
    print('===================================')












