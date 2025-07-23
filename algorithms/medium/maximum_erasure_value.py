from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        seen = set()
        curr = 0
        res = float('-inf')
        left, right = 0, 0
        while right < N:
            if nums[right] in seen:
                while True:
                    curr -= nums[left]
                    seen.remove(nums[left])
                    left += 1
                    if nums[left - 1] == nums[right]:
                        break
            seen.add(nums[right])
            curr += nums[right]
            res = max(res, curr)
            right += 1
        return res

# Main section
for nums in [
               [4,2,4,5,6],
               [5,2,1,2,5,2,1,2,5],
               [14,21,25,12,29,5,27,22,23,1,25,12,21,4,23,17,3,26,6,12,11,29,24,2,24,18,29,12,10,7,18,18,11,25,7,2,5,25,4,3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumUniqueSubarray(nums)
    print(f'r = {r}')
    print('============================')







