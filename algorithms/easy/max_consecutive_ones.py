from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        current_streak = 0
        in_window = False
        for i in nums:
            if i == 1:
                in_window = in_window or True
                current_streak += 1
            elif in_window:
                if i == 0:
                    in_window = False
                    max_streak = max(current_streak, max_streak)
                    current_streak = 0
        max_streak = max(current_streak, max_streak)
        return max_streak

# Main section
for nums in [
               [1,1,0,1,1,1],
               [1,0,1,1,0,1],
               [0,0,0,0,1,0,0,1,1,1],
               [1],
               [1,1,1,1],
               [0,0,0,0,0],
               [0],
            ]:
    sol = Solution()
    print(f'nums = {nums}')
    r = sol.findMaxConsecutiveOnes(nums)
    print(f'r = {r}')
    print('==========================')

