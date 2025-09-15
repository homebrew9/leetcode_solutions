from typing import List

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        # Leftmost index
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left < 0 or left >= N or nums[left] != target:
            return False
        leftmost_ind = left
        # Rightmost index
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0 or right >= N or nums[right] != target:
            return False
        rightmost_ind = right
        occurrences = rightmost_ind - leftmost_ind + 1
        return occurrences > N / 2

# Main section
for nums, target in [
                       ([2,4,5,5,5,5,5,6,6], 5),
                       ([10,100,101,101], 101),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.isMajorityElement(nums, target)
    print(f'r = {r}')
    print('===================')












