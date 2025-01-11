from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        #print(f'\tlow, high = {low}, {high}')
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            #print(f'\t\tlow, mid, high = {low}, {mid}, {high}')
        #print(f'\tlow, mid, high = {low}, {mid}, {high}')
        return low

# Main section
for nums, target in [
                       ([0,2,4,6,8,10,12], 15),
                       ([0,2,4,6,8,10,12], -7),
                       ([0,2,4,6,8,10,12], 3),
                       ([0,2,4,6,8,10,12], 10),
                       ([0,2,4,6,8,10,12], 11),
                       ([0,2,4,6,8,10,12],  7),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.searchInsert(nums, target)
    print(f'r = {r}')
    print('===================')

