from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # General case: P is pivot point, and is min value; P < C < A < B
        # A--------B-P------C
        # Now M (midpoint of Binary Search) can have P at the right or left/itself:
        # A--------M----B-P--C
        # A---B-P--M---------C
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # So we should search on the right, but confirm that first!
                if nums[left] <= nums[mid] <= nums[right]:
                    # Unrotated array, move to right
                    left = mid + 1
                elif nums[left] <= nums[mid] and nums[mid] >= nums[right]:
                    # Pivot point is on the right
                    left = mid + 1
                elif nums[mid] <= nums[right] and nums[left] >= nums[mid]:
                    # Pivot point is "mid" or on left
                    if nums[right] < target:
                        right = mid - 1
                    else:
                        left = mid + 1
            elif nums[mid] > target:
                if nums[left] <= nums[mid] <= nums[right]:
                    # Unrotated array
                    right = mid - 1
                elif nums[left] <= nums[mid] and nums[mid] >= nums[right]:
                    # Pivot point is on the right
                    if nums[left] > target:
                        left = mid + 1
                    else:
                        right = mid - 1
                elif nums[mid] <= nums[right] and nums[left] >= nums[mid]:
                    # Pivot point is in mid or on left
                    right = mid - 1
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
                       ([4,5,6,7,0,1,2], 0),
                       ([4,5,6,7,0,1,2], 1),
                       ([4,5,6,7,0,1,2], 2),
                       ([4,5,6,7,0,1,2], 3),
                       ([4,5,6,7,0,1,2], 4),
                       ([4,5,6,7,0,1,2], 5),
                       ([4,5,6,7,0,1,2], 6),
                       ([4,5,6,7,0,1,2], 7),
                       ([4,5,6,7,0,1,2], 8),
                       ([4,5,6,7,0,1,2], -1),
                       ([9], 0),
                       ([9], 9),
                       ([9], 11),
                       ([3,1], 0),
                       ([3,1], 1),
                       ([3,1], 3),
                       ([3,1], 5),
                       ([3,1], -9),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.search(nums, target)
    print(f'r = {r}')
    print('==============')

