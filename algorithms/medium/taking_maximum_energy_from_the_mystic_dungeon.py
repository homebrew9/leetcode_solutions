from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # Let's try to solve this by reverse traversal!
        N = len(energy)
        arr = [0 for _ in range(N)]
        res = -10**20
        for i in range(N-1, -1, -1):
            if i + k >= N:
                arr[i] = energy[i]
            else:
                arr[i] = energy[i] + arr[i+k]
            res = max(res, arr[i])
        return res

# Main section
for energy, k in [
                    ([5,2,-10,-5,1], 3),
                    ([-2,-3,-1], 2),
                 ]:
    print(f'energy, k = {energy}, {k}')
    sol = Solution()
    r = sol.maximumEnergy(energy, k)
    print(f'r = {r}')
    print('=====================')






