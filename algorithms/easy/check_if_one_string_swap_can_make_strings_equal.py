from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        cnt = 0
        for x, y in zip(s1, s2):
            if x != y:
                cnt += 1
        if cnt in (0, 2):
            return True
        else:
            return False

# Main section
for s1, s2 in [
                 ('bank', 'kanb'),
                 ('attack', 'defend'),
                 ('kelb', 'kelb'),
                 ('bank', 'knab'),
              ]:
    print(f's1, s2 = {s1}, {s2}')
    sol = Solution()
    r = sol.areAlmostEqual(s1, s2)
    print(f'r = {r}')
    print('=============================')

