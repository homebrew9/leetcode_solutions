from typing import List
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # ==========================================================================================
        # Why do we need the boolean "valid"? The way Binary Search works, if match_count ever
        # exceeds len(nums) then it should be able to approximate the required number of tries.
        # But there are cases like ([4,3,2,1], [[1,3,2],[0,2,1]]), where, even after all queries
        # are done, we have the prefix array: [1,3,3,2]. This array cannot be greater than
        # nums = [4,3,2,1] because we never exceeded nums at any time during Binary Search. That
        # is why we set valid to True inside the BSearch loop, so that we know from which side of
        # the fence we reached to the value of "left".
        # ==========================================================================================
        def determine_match_count(idx):
            diff = [0] * (M + 1)
            prfx = [0] * M
            for i in range(idx + 1):
                start_ind, end_ind, delta = queries[i]
                diff[start_ind] += delta
                diff[end_ind+1] -= delta
            for j in range(M):
                if j == 0:
                    prfx[j] = diff[j]
                else:
                    prfx[j] = prfx[j-1] + diff[j]
            return sum([prfx[i] >= nums[i] for i in range(M)])
        # Check if we need to start the process at all.
        if len(set(nums)) == 1 and list(set(nums))[0] == 0:
            return 0
        M = len(nums)
        N = len(queries)
        left, right = 0, N - 1
        valid = False
        while left <= right:
            mid = (left + right) // 2
            match_count = determine_match_count(mid)
            if match_count >= M:
                valid = True
                right = mid - 1
            else:
                left = mid + 1
        return left + 1 if valid else -1

# Main section
for nums, queries in [
                        ([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]),
                        ([4,3,2,1], [[1,3,2],[0,2,1]]),
                        ([2,7,6,8,6,1,6,5,3,1], [[0,4,1],[2,7,2],[4,9,3],[1,6,2],[0,5,4],[3,7,4],[1,3,1]]),
                     ]:
    print(f'nums, queries = {nums}, {queries}')
    sol = Solution()
    r = sol.minZeroArray(nums, queries)
    print(f'r = {r}')
    print('=================')

