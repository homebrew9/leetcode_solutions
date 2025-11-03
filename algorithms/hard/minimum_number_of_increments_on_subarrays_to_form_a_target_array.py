from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                res += target[i] - target[i-1]
        return res

# Main section
for target in [
                 [1,2,3,2,1],
                 [3,1,1,2],
                 [3,1,5,4,2],
              ]:
    print(f'target = {target}')
    sol = Solution()
    r = sol.minNumberOperations(target)
    print(f'r = {r}')
    print('=====================')











