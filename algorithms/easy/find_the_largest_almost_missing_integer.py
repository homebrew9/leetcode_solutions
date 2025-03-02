from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        def occurs_only_in_one(n):
            cnt = 0
            for lst in lst_subarrays:
                if n in lst:
                    cnt += 1
                    if cnt > 1:
                        return False
            return True
        N = len(nums)
        lst_subarrays = list()
        for i in range(0, N - k + 1):
            lst_subarrays.append(nums[i:i+k])
        res = -1
        for n in nums:
            if occurs_only_in_one(n):
                res = max(res, n)
        return res

# Main section
for nums, k in [
                  ([3,9,2,1,7], 3),
                  ([3,9,7,2,1,7], 4),
                  ([0,0], 1),
                  ([0,0], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.largestInteger(nums, k)
    print(f'r = {r}')
    print('================================')

