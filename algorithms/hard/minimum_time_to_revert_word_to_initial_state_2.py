#
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/solutions/4687845/kmp-o-n-neetcode-style/
#
import math
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        # LPS = Longest Prefix Suffix
        LPS = [0] * len(word)

        prevLPS, i = 0, 1
        while i < len(word):
            if word[i] == word[prevLPS]:
                LPS[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                i += 1
            else:
                prevLPS = LPS[prevLPS - 1]

        # second conditions check if removed length is valid (multiple of k)
        # if not, find previous matching prefix
        while prevLPS and (len(word) - prevLPS) % k > 0:
            prevLPS = LPS[prevLPS - 1]

        lenToBeRemoved = len(word) - prevLPS
        return math.ceil(lenToBeRemoved / k)


# Main section
for word, k in [
                   ('abacaba', 3),
                   ('abacaba', 4),
                   ('abcbabcd', 2),
               ]:
    print(f'word, k = {word}, {k}')
    sol = Solution()
    r = sol.minimumTimeToInitialState(word, k)
    print(f'r = {r}')
    print('=========================')

