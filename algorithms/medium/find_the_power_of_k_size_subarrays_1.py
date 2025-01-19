from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        diff = [0] + [nums[i] - nums[i-1] for i in range(1, N)]
        #print(diff)
        res = list()
        for i in range(k-1, N):
            diff_set = set(diff[i-k+2:i+1])
            #print(i, diff_set)
            if len(diff_set) == 0:
                res.append(nums[i])
            elif len(diff_set) == 1 and list(diff_set)[0] == 1:
                res.append(nums[i])
            else:
                res.append(-1)
        return res

# Main section
for nums, k in [
                  ([1,2,3,4,3,2,5], 3),
                  ([2,2,2,2,2], 4),
                  ([3,2,3,2,3,2], 2),
                  ([3,2,3,2,3,2], 1),
                  ([1,2,3,4,5], 3),
                  ([1,2,3,4,5], 4),
                  ([1,2,3,4,5], 5),
                  ([5,4,3,2,1], 2),
                  ([5,4,3,2,1], 1),
                  ([3,2,4,5,1,1,10,9,9,8,3,8,5,8,7,2,5,7,10,8,9,7,5,1,9,6,8,9,10,5,8,1,3,4,4,7,4,4,2,8,2,8,6,9,4,5,1,3,6,6,7,6,10,4,7,5,4,4,4,3,10,3,5,5,10,6,10,1,10,10,10,6,8,7,5,1,9,8,10,6,3,4,8,1,4,3,7,7,5,10,4,3,4,10,1,10,6,5,4,6], 2),
                  ([3,2,4,5,1,1,10,9,9,8,3,8,5,8,7,2,5,7,10,8,9,7,5,1,9,6,8,9,10,5,8,1,3,4,4,7,4,4,2,8,2,8,6,9,4,5,1,3,6,6,7,6,10,4,7,5,4,4,4,3,10,3,5,5,10,6,10,1,10,10,10,6,8,7,5,1,9,8,10,6,3,4,8,1,4,3,7,7,5,10,4,3,4,10,1,10,6,5,4,6], 3),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.resultsArray(nums, k)
    print(f'r = {r}')
    print('==================')


