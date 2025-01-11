from typing import List
from collections import Counter, deque

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Beautiful problem! Rearrange the elements ordered by their decreasing
        # frequencies and append them to a deque. Then popleft the elements
        # from the deque and set them at alternate locations in the final array.
        # barcodes = [1,1,1,2,3,2,3]
        # dq = [1,1,1,2,2,3,3] .......... (Case A)
        #     After 1st loop: res = [1, None, 1, None, 1, None, 2]
        #     After 2nd loop: res = [1, 2, 1, 3, 1, 3, 2]
        # dq = [1,1,1,3,3,2,2] .......... (Case B)
        #     After 1st loop: res = [1, None, 1, None, 1, None, 3]
        #     After 2nd loop: res = [1, 3, 1, 2, 1, 2, 3]
        N = len(barcodes)
        res = [None for _ in range(N)]
        cntr = Counter(barcodes)
        dq = deque()
        for k, v in sorted([(k, v) for k, v in cntr.items()], key=lambda x: -x[1]):
            for _ in range(v):
                dq.append(k)
        for i in range(0, N, 2):
            res[i] = dq.popleft()
        for i in range(1, N, 2):
            res[i] = dq.popleft()
        return res

# Main section
for barcodes in [
                   [1,1,1,2,2,2],
                   [1,1,1,1,2,2,3,3],
                   [2,1,1],
                   [7,7,7,8,5,7,5,5,5,8],
                   [1,1,2],
                   [1],
                   [1,1,1,2,2,3,3],
                ]:
    print(f'barcodes = {barcodes}')
    sol = Solution()
    r = sol.rearrangeBarcodes(barcodes)
    print(f'r = {r}')
    print('==================')

