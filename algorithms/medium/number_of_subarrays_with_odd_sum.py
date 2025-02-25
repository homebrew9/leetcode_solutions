from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
             [1, 3, 5]
             [1, 4, 9]
             ================================
             [1, 2, 3,  4,  5,  6,  7]
             [1, 3, 6, 10, 15, 21, 28]
             [1, 1, 2,  2,  3,  3,  4]  = 16
        '''
        MOD = 10**9 + 7
        N = len(arr)
        pfx = [0 for _ in range(N)]
        for i in range(N):
            pfx[i] = arr[i] if i == 0 else pfx[i-1] + arr[i]
        odd_count, even_count = 0, 0
        res = 0
        for i in range(N):
            if pfx[i] % 2 == 1:
                res = (res + 1 + even_count) % MOD
                odd_count += 1
            else:
                res = (res + odd_count) % MOD
                even_count += 1
        return res

# Main section
for arr in [
              [1,3,5],
              [2,4,6],
              [1,2,3,4,5,6,7],
              [52,53,91,86,24,83,26,12,33,31,44,31,70,96,93,24,53,43,92,71,99,14,38,2,58,90,30,22,45,26,17,100,99,1,100,79,33,98,6,47,85,80,39,83,58,33,82,69,11,44],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.numOfSubarrays(arr)
    print(f'r = {r}')
    print('==========================')

