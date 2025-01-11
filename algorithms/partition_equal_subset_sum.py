from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        nums.sort()
        lptr = 0
        lsum = nums[lptr]
        rptr = len(nums) - 1
        rsum = nums[rptr]
        print(nums)
        while lptr < rptr:
            print(f'\t>>> lptr, rptr = {lptr}, {rptr}')
            if lsum < rsum:
                lptr += 1
                lsum += nums[lptr]
            elif lsum > rsum:
                rptr -= 1
                rsum += nums[rptr]
            else:
                if rptr == lptr + 1:
                    return True
                else:
                    lptr += 1
                    lsum += nums[lptr]
                    rptr -= 1
                    rsum += nums[rptr]
        return False

# Main section
sol = Solution()
for nums in [
               #[1,5,11,5],
               #[1,2,3,5],
               #[1,5,6,8,9,11],
               #[1],
               #[7],
               #[2,3],
               #[4,4],
               #[1,1,7,1,1,1,1,1,6,1,1,1,1,1,1],
               #[1,3,4,4],
               #[1,1,1,1,1,1,1,1],
               [2,2,1,1],
            ]:
    print(f'nums = {nums}')
    r = sol.canPartition(nums)
    print(f'r    = {r}')
    print('==================================')

