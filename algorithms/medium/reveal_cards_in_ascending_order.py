#
# I did the simulation and found out a pattern that could be used.
# However, LC solution uses a deque in a VERY ELEGANT solution!!
#
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) <= 2:
            return deck
        N = len(deck)
        deck.sort()
        arr = list()
        arr.append(deck[N-1])
        arr.append(deck[N-2])
        for i in range(N-3, -1, -1):
            arr.append(0)
            arr.append(deck[i])
        # Two pointer run in the list "arr"
        M = len(arr)
        left, right = 0, 2
        while right < M:
            arr[right] = arr[left]
            right += 2
            left += 1
        return arr[-N:][::-1]

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

