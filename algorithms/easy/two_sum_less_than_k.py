from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        '''
            sorted(nums) = [1, 8, 23, 24, 33, 34, 54, 75], k = 60
        '''
        N = len(nums)
        nums.sort()
        #print(nums)
        res = -1
        for i in range(N-1):
            val = k - nums[i]
            #print(f'\ti, nums[i], val = {i}, {nums[i]}, {val}')
            left = i + 1
            right = N - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= val:
                    right = mid - 1
                else:
                    left = mid + 1
            #print(f'\t\tright, nums[right] = {right}, {nums[right]}')
            if i != right and nums[i] + nums[right] < k:
                res = max(res, nums[i] + nums[right])
                #print(f'\t\tnums[i] + nums[right] = {nums[i] + nums[right]}')
        return res

# Main section
for nums, k in [
                  ([34,23,1,24,75,33,54,8], 60),
                  ([10,20,30], 15),
                  ([254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944], 200),
                  ([358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549], 1800),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.twoSumLessThanK(nums, k)
    print(f'r = {r}')
    print('==================')


