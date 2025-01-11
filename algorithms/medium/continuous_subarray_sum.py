from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #hsh = dict()
        hsh = {0: 0}
        s = 0
        for i in range(len(nums)):
            print(f'\t\ti, nums[i], hsh = {i}, {nums[i]}, {hsh}')
            s += nums[i]
            # if remainder s%k occurs for the first time
            if s%k not in hsh:
                hsh[s%k] = i + 1
            elif hsh[s%k] < i:
                #subarray size is at least 2
                return True
        print(f'\thsh = {hsh}')
        return False

# Main section
for nums, k in [
                  ([23,2,4,6,7], 6),
                  ([23,2,6,4,7], 13),
                  ([5,0,0,], 3),
                  ([1,1,1,1,1], 5),
                  ([1,2,3,4,5], 15),
                  ([1,2,3,4,5], 16),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.checkSubarraySum(nums, k)
    print(f'r = {r}')
    print('=====================')

