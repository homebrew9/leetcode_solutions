#
# Easy problem, we just need to iterate over numbers and keep distance dist to the last occurence of 1.
#     If we meet 0, we need to increase distance by 1.
#     If we meet 1 and current distance is more or equal than k, than everything is OK and we need to update dist = 0.
#     If we meet 1 and current distance is less than k, than there will be two 1 placed less than k indexes away, so we can immedietly return False.
#     In the end we return True if we reached this place.
#
from typing import List

class Solution:
    def kLengthApart(self, nums, k):
        dist = k
        for num in nums:
            if num == 0:
                dist += 1
            elif num == 1 and dist >= k:
                dist = 0
            else:
                return False
        return True

# Main section
for nums, k in [
                  ([1,0,0,0,1,0,0,1], 2),
                  ([1,0,0,1,0,1], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.kLengthApart(nums, k)
    print(f'r = {r}')
    print('===================')

