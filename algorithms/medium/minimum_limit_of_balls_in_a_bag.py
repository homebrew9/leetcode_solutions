from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def is_split_possible(p):
            # Is it possible to split nums in maxOperations or less operations
            # while keeping the max penalty as p? True if yes, False otherwise.
            cnt = 0
            for n in nums:
                if n > p:
                    if n % p == 0:
                        cnt += n // p - 1
                    else:
                        cnt += int(n / p)
                if cnt > maxOperations:
                    return False
            return True
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            if is_split_possible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

# Main section
for nums, maxOperations in [
                              ([9], 2),
                              ([2,4,8,2], 4),
                              ([57,51,54,51,62,37,67,81,33,5,35,37,80,83,72,40,60,8,27,73,35,21,70,29,22,62,82,80,86,33,31,64,99,98,82,84,43,82,93,60,48,66,100,39,86,28,40,51,26,6,37,24,75], 6),
                           ]:
    print(f'nums, maxOperations = {nums}, {maxOperations}')
    sol = Solution()
    r = sol.minimumSize(nums, maxOperations)
    print(f'r = {r}')
    print('================')


