from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0 for _ in range(length)]
        for i, j, k in updates:
            nums[i] = nums[i] + k
            if j + 1 < length:
                nums[j+1] = nums[j+1] - k
        for i in range(1, length):
            nums[i] = nums[i-1] + nums[i]
        return nums

# Main section
for length, updates in [
                          (5, [[1,3,2],[2,4,3],[0,2,-2]]),
                          (10, [[2,4,6],[5,6,8],[1,9,-4]]),
                       ]:
    print(f'length, updates = {length}, {updates}')
    sol = Solution()
    r = sol.getModifiedArray(length, updates)
    print(f'r = {r}')
    print('===========================')













