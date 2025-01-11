from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Number of zeros in the window
        zeroCount = 0
        longestWindow = 0
        # Left end of the window
        start = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            # Shrink the window until the zero counts come under the limit
            while zeroCount > 1:
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1
            longestWindow = max(longestWindow, i - start)
        return longestWindow

# Main section
for nums in [
               [1,1,0,1],
               [0,1,1,1,0,1,1,0,1],
               [1,1,1],
               [1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1],
               [1,1,1,1,1,1,1],
               [1,1,1,1,1,1,0],
               [0,0,1,1,1,1,1,0,0,1,1,0,1,0],
               [0,0,0,0,0,0,0],
               [0,0,1,1],
               [1,0,1,1,1,1,1,1,0,1,1,1,1,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.longestSubarray(nums)
    print(f'r = {r}')
    print('===================')




