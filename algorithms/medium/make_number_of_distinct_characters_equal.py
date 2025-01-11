#
# Did not work during contest!!
# The trick is to try all combinations of swaps from both Counters!!
#
from collections import Counter
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cntr1 = Counter(word1)
        cntr2 = Counter(word2)
        M = len(cntr1)
        N = len(cntr2)
        s1 = set(cntr1.keys())
        s2 = set(cntr2.keys())
        if M == N:
            return True
        if M == N + 1:
            if len(s1.intersection(s2)) > 0:
                return True
            return max(cntr2.values()) > 1
        elif N == M + 1:
            if len(s1.intersection(s2)) > 0:
                return True
            return max(cntr1.values()) > 1
        return False

# Main section
for word1, word2  in [
                        ('ab', 'abcc'),
                     ]:
    print(f'word1, word2 = {word1}, {word2}')
    sol = Solution()
    r = sol.isItPossible(word1, word2)
    print(f'r = {r}')
    print('=================')

