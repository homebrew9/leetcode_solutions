from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # The core idea here is to create an array that has alternate bits and their streaks.
        # For example, for nums = [0,1,1,1,0,1,1,0,1] we form the array arr = [(0,1),(1,3),(0,1),(1,2),(0,1),(1,1)]
        # Then we simply iterate through arr to check three things:
        #   a) The longest streak for 1, say, x
        #   b) The longest streak (m+n) for elements like  [...(1,m),(0,1),(1,n)...] Let's say it is y.
        #   c) If at least one zero was found
        # If no zero was found, then the answer is x - 1. Otherwise it is the max of x and y.
        # TC = O(N), SC = O(N)
        N = len(nums)
        curr = nums[0]
        arr = list()
        i, j = 0, 1
        while j < N:
            if nums[j] != curr:
                arr.append((curr, j - i))
                curr = nums[j]
                i = j
            j += 1
        arr.append((curr, j - i))
        M = len(arr)
        res1, res2 = 0, 0
        no_zeros = True
        for i in range(M):
            bit, span = arr[i]
            if bit == 1:
                res1 = max(res1, span)
                if i <= M - 3:
                    if arr[i+1][1] == 1:
                        res2 = max(res2, span + arr[i+2][1])
            else:
                no_zeros = False
        return res1 - 1 if no_zeros else max(res1, res2)

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












