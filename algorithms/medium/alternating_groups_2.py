from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Sliding window logic
        arr = colors + colors[:k-1]
        N = len(arr)
        i = 0
        res = 0
        for j in range(1, N):
            if arr[j] + arr[j-1] == 1:
                if j - i + 1 == k:
                    res += 1
                    i += 1
            else:
                i = j
        return res

# Main section
for colors, k in [
                    ([0,1,0,1,0], 3),
                    ([0,1,0,0,1,0,1], 6),
                    ([1,1,0,1], 4),
                 ]:
    print(f'colors, k = {colors}, {k}')
    sol = Solution()
    r = sol.numberOfAlternatingGroups(colors, k)
    print(f'r = {r}')
    print('=========================')

