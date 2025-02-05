class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        a, b, c, d = None, None, None, None
        for x, y in zip(s1, s2):
            if x != y:
                diff += 1
                if diff == 1:
                    a, b = x, y
                elif diff == 2:
                    c, d = x, y
                else:
                    return False
        return (a, b) == (d, c)

# Main section
for s1, s2 in [
                 ('bank', 'kanb'),
                 ('attack', 'defend'),
                 ('kelb', 'kelb'),
                 ('bank', 'knab'),
                 ('caa', 'aaz'),
              ]:
    print(f's1, s2 = {s1}, {s2}')
    sol = Solution()
    r = sol.areAlmostEqual(s1, s2)
    print(f'r = {r}')
    print('=============================')

