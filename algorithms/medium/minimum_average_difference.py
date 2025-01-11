from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        size = len(nums)
        total = sum(nums)
        left_sum, right_sum = 0, 0
        min_avg_diff = float('inf')
        ind = None
        for i, v in enumerate(nums):
            left_sum += v
            right_sum = total - left_sum
            print(f'\tleft_sum, right_sum = {left_sum}, {right_sum}')
            left_avg = left_sum // (i+1)
            if size - i - 1 == 0:
                right_avg = 0
            else:
                right_avg = right_sum // (size - i - 1)
            print(f'\t\tleft_avg, right_avg = {left_avg}, {right_avg}')
            avg_diff = abs(left_avg - right_avg)
            if avg_diff < min_avg_diff:
                min_avg_diff = avg_diff
                ind = i
            print(f'\t\tavg_diff = {avg_diff}')
        return ind

# Main section
for nums in [
               [2,5,3,9,5,3],
               [0],
               [1,2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minimumAverageDifference(nums)
    print(f'r = {r}')
    print('================')

