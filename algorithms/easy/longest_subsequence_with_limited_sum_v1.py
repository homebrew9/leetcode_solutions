from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        size = len(nums)
        prefix_sum = 0
        for i in range(size):
            prefix_sum += nums[i]
        arr = list()
        #print(f'\tnums = {nums}')
        for q in queries:
            #print(f'\t\tq = {q}')
            low, high = 0, size - 1
            while low <= high:
                mid = (low + high) // 2
                #print(f'\t\tlow, mid, high = {low}, {mid}, {high}')
                if sum(nums[:mid+1]) > q:
                    high = mid - 1
                else:
                    low = mid + 1
            #print(f'\tlow, mid, high, nums[:low] = {low}, {mid}, {high}, {nums[:low]}')
            #print('=====')
            arr.append(len(nums[:low]))
        return arr

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

