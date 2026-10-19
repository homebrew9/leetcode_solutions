class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        N = len(nums)
        max_total = -10**20
        a, b = -1, -1
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] + nums[j] == target and nums[i] != nums[j]:
                    if (mx := nums[i] * nums[j]) > max_total:
                        max_total = mx
                        a = i if nums[i] > nums[j] else j
                        b = i if nums[i] < nums[j] else j
        return [a, b]

# Main section
for nums, target in [
                       ([1,2,3,4], 5),
                       ([-3,-1,4,2], 1),
                       ([3,3,5], 6),
                       ([4,5,-6,-7], -2),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.maxProductPair(nums, target)
    print(f'r = {r}')
    print('===================================')
















