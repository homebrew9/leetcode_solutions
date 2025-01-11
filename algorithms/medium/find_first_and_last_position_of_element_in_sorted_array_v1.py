from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        arr = list()
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        #print(f'low, size = {low}, {len(nums)}')
        if low < 0 or low >= len(nums) or nums[low] != target:
            return [-1, -1]
        arr.append(low)
        # Binary Search again to determine the rightmost index
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        arr.append(high)
        return arr

# Main section
for nums, target in [
                       ([5,7,7,8,8,10], 8),
                       ([5,7,7,8,8,10], 6),
                       ([], 0),
                       ([1], 0),
                       ([1], 1),
                       ([1], 2),
                       ([1,2,3,4,5,6,7,8,9,9,9,9,10], 9),
                       ([1,2,3,4,5,6,7,8,9,9,9,9,10], 5),
                       ([1,2,3,4,5,6,7,8,9,9,9,9,10], -9),
                       ([1,2,3,4,5,6,7,8,9,9,9,9,10], 99),
                       ([1,2,3,4,4,5,6,7,8,9,9,9,9,10], 4),
                       ([1,2,3,4,4,5,6,7,8,9,9,9,9,10], 1),
                       ([1,2,3,4,4,5,6,7,8,9,9,9,9,10], 10),
                       ([1,2,3,3,3,4,5,6,6,7,7,7,7,7,7,7,8,9], 7),
                       ([1,2,3,3,3,4,5,6,6,7,7,7,7,7,7,7,8,9], 4),
                       ([1,2,3,3,3,4,5,6,6,7,7,7,7,7,7,7,8,9], 1),
                       ([1,2,3,3,3,4,5,6,6,7,7,7,7,7,7,7,8,9], 9),
                       ([1,2,3,3,3,4,5,6,6,7,7,7,7,7,7,7,8,9], 0),
                       ([1,2,3,3,3,4,5,6,6,7,7,7,7,7,7,7,8,9], 10),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.searchRange(nums, target)
    print(f'r = {r}')
    print('=====================')

