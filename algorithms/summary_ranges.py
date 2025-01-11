from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        arr = list()
        s = None
        count = 0
        for i, n in enumerate(nums):
            if i == 0:
                s = str(n)
                count += 1
            elif n - nums[i-1] > 1:
                if count > 1:
                    s += '->' + str(nums[i-1])
                arr.append(s)
                s = str(n)
                count = 1
            else:
                count += 1

        # Done with the list nums; now handle the last element
        if count > 1:
            s += '->' + str(nums[-1])
        arr.append(s)
        return arr

# Main section
sol = Solution()
for nums in [
               [0,1,2,3,4,9,10,11,15],
               [0,1,2,3,4,9,10,11,12],
               [0,2,4,10,12],
               [0,1,2,4,5,7],
               [0,2,3,4,6,8,9],
               [],
               [-1],
               [0],
            ]:
    print(f'nums = {nums}')
    r = sol.summaryRanges(nums)
    print(f'r    = {r}')
    print('===========================')


