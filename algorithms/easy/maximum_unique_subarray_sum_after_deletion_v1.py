from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        hsh = {'pos': 0, 'neg': 0, 'zero': 0}
        for n in nums:
            if n > 0:
                hsh['pos'] += 1
            elif n < 0:
                hsh['neg'] += 1
            else:
                hsh['zero'] += 1
        if hsh['pos'] == 0:
            return max(nums)
        else:
            seen = set()
            res = 0
            for n in nums:
                if n > 0 and n not in seen:
                    res += n
                    seen.add(n)
            return res
 
# Main section
for nums in [
               [1,2,3,4,5],
               [1,1,0,1,1],
               [1,2,-1,-2,1,0,-1],
           ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxSum(nums)
    print(f'r  = {r}')
    print('================')

