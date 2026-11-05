class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        N = len(nums)
        res = 10**20
        for i in range(1,N,2):
            prev, curr = nums[i-1], nums[i]
            factor = 1
            while curr > 0:
                q, r = divmod(curr, 10)
                factor *= 10
                curr = q
            val = prev * factor + nums[i]
            res = min(res, val)
        return res

# Main section
for nums in [
               [23,55,42,21],
               [34,7,11,11],
               [9,20],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minMergedInteger(nums)
    print(f'r = {r}')
    print('===================================')









