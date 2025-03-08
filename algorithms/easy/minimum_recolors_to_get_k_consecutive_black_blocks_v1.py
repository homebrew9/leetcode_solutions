#
# Study this sliding window technique very carefully!!
# 1) Maintain a sliding window of length k.
# 2) Keep a score of 'W' characters in each sliding window.
# 3) The minimum count of 'W' across all sliding windows is the answer.
#
from typing import List

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)
        res = blocks[:k].count('W')
        curr = res
        for i in range(k, N):
            curr += (blocks[i] == 'W') - (blocks[i-k] == 'W')
            res = min(res, curr)
        return res

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

