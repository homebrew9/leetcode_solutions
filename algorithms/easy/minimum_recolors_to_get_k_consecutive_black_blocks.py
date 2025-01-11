#
# Study this sliding window technique very carefully!!
# 1) Maintain a sliding window of length k.
# 2) Keep a score of 'W' characters in each sliding window.
# 3) The minimum count of 'W' across all sliding windows is the answer.
#
from typing import List

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        left, right = 0, 0
        cnt = 0
        min_cnt = float('inf')
        for left in range(0, n-k+1):
            #print(f'\tleft = {left}')
            if left == 0:
                for right in range(k):
                    if blocks[right] == 'W':
                        cnt += 1
                min_cnt = min(min_cnt, cnt)
            else:
                if blocks[left-1] == 'W':
                    cnt -= 1
                right += 1
                if blocks[right] == 'W':
                    cnt += 1
                min_cnt = min(min_cnt, cnt)
            #print(f'\tright = {right}')
            #print(f'\t\tcnt = {cnt}')
            #print(f'\t\tmin_cnt = {min_cnt}')
        return min_cnt

# Main section
for blocks, k in [
                    ('WBBWWBBWBW', 7),
                    ('WBBWWBWWBW', 7),
                    ('WBBWWBBBBB', 7),
                    ('WBWBBBW', 2)
                 ]:
    print(f'blocks, k = {blocks}, {k}')
    sol = Solution()
    r = sol.minimumRecolors(blocks, k)
    print(f'r = {r}')
    print('=======================')

