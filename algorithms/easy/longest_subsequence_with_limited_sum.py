from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for q in queries:
            #print(f'\tq = {q}')
            cnt = 0
            curr_sum = 0
            for i, v in enumerate(nums):
                if curr_sum + v <= q:
                    cnt += 1
                    curr_sum += v
                else:
                    break
            ans += [cnt]
        return ans

# Main section
for nums, queries in [
                        ([4,5,2,1], [3,10,21]),
                        ([2,3,4,5], [1]),
                        ([1,2,3,4], [1]),
                        ([5,4,3,2,1], [7,9]),
                        ([736411,184882,914641,37925,214915], [331244,273144,118983,118252,305688,718089,665450]),
                        ([469781,45635,628818,324948,343772,713803,452081], [816646,929491]),
                     ]:
    print(f'nums = {nums}, queries = {queries}')
    sol = Solution()
    r = sol.answerQueries(nums, queries)
    print(f'r = {r}')
    print('=====================')

