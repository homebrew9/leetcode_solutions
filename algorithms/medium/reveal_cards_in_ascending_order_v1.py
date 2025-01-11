#
# LC solution - very elegant!
#
from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        index = deque(range(N))
        ans = [None] * N
        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
        return ans

# Main section
for deck in [
              [17,13,11,2,3,5,7],
              [1,1000],
              [2,3,4,5,6,7,8,9,10,11,12,13],
              [2],
              [2,3],
              [2,3,4],
              [2,3,4,5],
              [2,3,4,5,6],
              [2,3,4,5,6,7],
              [664,879,952,272,976,288,979,17,857,866,910,934,469,811,45,895,268,321,125,543],
            ]:
    print(f'deck = {deck}')
    sol = Solution()
    r = sol.deckRevealedIncreasing(deck)
    print(f'r = {r}')
    print('========================')


