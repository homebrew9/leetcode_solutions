from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        N = len(arr)
        seen = set()
        for n in arr:
            seen.add(n)
        res = 0
        for i in range(0, N-2):
            for j in range(i+1, N-1):
                x, y = arr[i], arr[j]
                length = 2
                while (z := x + y) in seen:
                    length += 1
                    x, y = y, z
                    res = max(res, length)
        return res

# Main section
for arr in [
              [1,2,3,4,5,6,7,8],
              [1,3,7,11,12,14,18],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.lenLongestFibSubseq(arr)
    print(f'r = {r}')
    print('========================')

