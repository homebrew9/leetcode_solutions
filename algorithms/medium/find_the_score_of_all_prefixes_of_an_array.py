from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        N = len(nums)
        max_so_far = 0
        arr_conv = [None for _ in range(N)]
        for i, n in enumerate(nums):
            max_so_far = max(max_so_far, n)
            arr_conv[i] = n + max_so_far
        arr_score = [None for _ in range(N)]
        sum_so_far = 0
        for i, n in enumerate(arr_conv):
            sum_so_far += n
            arr_score[i] = sum_so_far
        return arr_score

# Main section
for nums in [
               [2,3,7,5,10],
               [1,1,2,4,8,16],
               [5],
               [5,6],
               [5,6,7],
               [10,20,3,8,99,45,20],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findPrefixScore(nums)
    print(f'r = {r}')
    print('==================')

