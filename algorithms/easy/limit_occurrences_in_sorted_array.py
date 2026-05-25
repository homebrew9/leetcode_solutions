class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        prev = 0
        count = 0
        res = list()
        for n in nums:
            if n != prev and count > 0:
                res.extend([prev] * count)
                count = 1
            elif count < k:
                count += 1
            prev = n
        res.extend([prev] * count)
        return res

# Main section
for nums, k in [
                  ([1,1,1,2,2,3], 2),
                  ([1,2,3], 1),
                  ([1], 1),
                  ([1,1,1,2,2,2,2,2,3,3,4], 3),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.limitOccurrences(nums, k)
    print(f'r = {r}')
    print('==================================')















