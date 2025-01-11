from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

# Main section
for nums, target in [
                       ([4,5,6,7,0,1,2], 0),
                       ([4,5,6,7,0,1,2], 3),
                       ([1], 0),
                       ([59,63,71,84,91,92,0,1,2,5,7,9,11,13,14,23,57], 3),
                       ([59,63,71,84,91,92,0,1,2,5,7,9,11,13,14,23,57], 13),
                       ([59,63,71,84,91,92,0,1,2,5,7,9,11,13,14,23,57], 99),
                       ([59,63,71,84,91,92,0,1,2,5,7,9,11,13,14,23,57], 58),
                       ([59,63,71,84,91,92,0,1,2,5,7,9,11,13,14,23,57], 57),
                       ([59,63,71,84,91,92,0,1,2,5,7,9,11,13,14,23,57], 59),
                       ([59,63,71,84,91,92,0,1,2,5,7,9,11,13,14,23,57], 0),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.search(nums, target)
    print(f'r = {r}')
    print('==============')

