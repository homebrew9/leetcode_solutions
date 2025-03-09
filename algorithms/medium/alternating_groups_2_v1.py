from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Sliding window logic
        '''
           colors = [0,1,0,1,0], k = 3
           arr    = [0,1,0,1,0,0,1]
        '''
        arr = colors + colors[:k-1]
        N = len(arr)
        res = 0
        cnt = 1
        for i in range(1, N):
            if arr[i-1] != arr[i]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                res += 1
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

