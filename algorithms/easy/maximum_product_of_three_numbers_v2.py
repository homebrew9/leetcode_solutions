from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        # Find the 2 least and 3 highest values in the list
        # by a single scan. The greatest product is the max
        # of min1*min2*max1 and max1*max2*max3
        min1 = 1001
        min2 = 1001
        max1 = -1001
        max2 = -1001
        max3 = -1001
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:    # n is between min1 and min2
                min2 = n

            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:    # n is between max2 and max1
                max3 = max2
                max2 = n
            elif n >= max3:    # n is between max3 and max2
                max3 = n
        return max(min1*min2*max1, max1*max2*max3)


# Main section
for nums in [
               [1,2,3],
               [0,1,2],
               [9,0,76,-9,3,37,-99,5],
               [1,2,3,4,5,6,7],
               [-9,-9,0,3,5,9,37,76],
               [-10,-8,-6,6,8,10],
               [-9,-8,-7,4,5,6],
               [-10,-9,-8,1,2,3],
               [-9,-8,-7,-6],
               [-9,-8,2,3],
               [-9,-7,-5,-3,0,1,4,6,7],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumProduct(nums)
    print(f'r = {r}')
    print('===========================')




