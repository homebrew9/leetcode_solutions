from typing import List

#class Solution:
#    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#        # Brute force method by generating all subsets 
#        def subsets(lst, i, n):
#            if len(lst) >= n:
#                res.append(lst)
#                return
#            if i >= N:
#                return
#            for j in range(i, N):
#                subsets(lst + [strs[j]], j+1, n)
#        N = len(strs)
#        res = list()
#        for size in range(1, N+1):
#            for i, v in enumerate(strs):
#                subsets([v], i+1, size)
#        ans = 0
#        for item in res:
#            zeros, ones = 0, 0
#            for v in item:
#                zeros += v.count('0')
#                ones += v.count('1')
#            if zeros <= m and ones <= n:
#                ans = max(ans, len(item))
#        return ans

# 
# Brute force to generate all subsets - from the editorial!
#
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count_zeros_ones(s):
            c = [0,0]
            for ch in s:
                c[int(ch)] += 1
            return c
        N = len(strs)
        maxlen = 0
        for i in range(0, 1<<N):
            print(f'i = {i}')
            zeros, ones, size = 0, 0, 0
            for j in range(0, N):
                print(f'\ti, j, 1<<j, (i&(1<<j)) = {i}, {j}, {1<<j}, {i&(1<<j)}')
                if i & (1<<j) != 0:
                    count = count_zeros_ones(strs[j])
                    zeros += count[0]
                    ones += count[1]
                    size += 1
            if zeros <= m and ones <= n:
                maxlen = max(maxlen, size)
        return maxlen


# Main section
for strs, m, n in [
                     (['10','0001','111001','1','0'], 5, 3),
                  ]:
    print(f'strs = {strs}')
    sol = Solution()
    r = sol.findMaxForm(strs, m, n)
    print(f'r = {r}')
    print('================')


