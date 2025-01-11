class Solution:
    #def solve(self, nums, k):
    #    nums.sort()
    #    left, right = 0, len(nums) - 1
    #    while left < right:
    #        if nums[left] + nums[right] > k:
    #            right -= 1
    #        elif nums[left] + nums[right] < k:
    #            left += 1
    #        else:
    #            return True
    #    return False

    def solve(self, nums, k):
        hsh = dict()
        for n in nums:
            if k - n in hsh:
                return True
            hsh[n] = 1
        return False

# Main section
for nums, k in [
                  ([35,8,18,3,22], 11),
                  ([10,36,22,14], 4),
                  ([24,10,11,4], 15),
                  ([-22,22,-11,11], 0),
                  ([15,0,3,2], 15),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.solve(nums, k)
    print(f'r = {r}')
    print('==========================')

