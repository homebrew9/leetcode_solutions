from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            curr = (1 if nums[i] % 2 == 1 else -1)
            seen = {nums[i]}
            for j in range(i+1, N):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    curr += (1 if nums[j] % 2 == 1 else -1)
                if curr == 0:
                    res = max(res, j - i + 1)
        return res

# Main section
for nums in [
               [2,5,4,3],
               [3,2,2,5,4],
               [1,2,3,2],
               [35,94,16,49,99,23,87,40,23,36,51,73,40,16,61,88,36,32,70,14,10,43,79,57,97,16,8,92,87,38,23,73,87,6,59,98,38,93,5,16],
               [3,4,6,2,10,1,4,6,8,8,6,1,3,6,4,4,2,10,9,3,7,1,1,8,2,7,9,6,5,9,3,3,10,8,2,9,8,6,4,7],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.longestBalanced(nums)
    print(f'r = {r}')
    print('=================================================')
 

















