from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Use Binary Search for O(logN) complexity
        def sign(x):
            if x > 0: return 1
            if x < 0: return -1
            return 0
        N = len(nums)
        # (a) Find rightmost index of zero
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if sign(nums[mid]) <= 0:
                left = mid + 1
            else:
                right = mid - 1
        rightmost_idx = left
        if rightmost_idx == 0:
            return N
        # (b) Find leftmost index of zero
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if sign(nums[mid]) >= 0:
                right = mid - 1
            else:
                left = mid + 1
        leftmost_idx = left
        if leftmost_idx >= N:
            return N
        #print(N, rightmost_idx, leftmost_idx)
        negative_count = leftmost_idx
        positive_count = N - rightmost_idx
        return max(positive_count, negative_count)

# Main section
for nums in [
               [-2,-1,-1,1,2,3],
               [-3,-2,-1,0,0,1,2],
               [5,20,66,1314],
               [-7,-6,-5,-4,-3,-2,-1,0,0,0,0,0,0,0,0,0,0,0,1],
               [-7,-6,-5,5,6,7],
               [-7,-6,-5,-4,-3,-2,-1,0],
               [-7,-6,-5,-4,-3,-2,-1],
               [-7,-6,-5,5,6,7,8],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maximumCount(nums)
    print(f'r = {r}')
    print('=================')

