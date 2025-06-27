class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        if s1 in s2:
            return s2
        if s2 in s1:
            return s1
        N, M = len(s1), len(s2)
        candidate1, ind = None, None
        for i in range(N-1, -1, -1):
            if s2.startswith(s1[i:]):
                ind = i
        if ind is not None:
            candidate1 = s1 + s2[N-ind:]
        candidate2, ind = None, None
        for j in range(M-1, -1, -1):
            if s1.startswith(s2[j:]):
                ind = j
        if ind is not None:
            candidate2 = s2 + s1[M-ind:]
        #print(f'\tcandidate1 = {candidate1}')
        #print(f'\tcandidate2 = {candidate2}')
        if candidate1 is None and candidate2 is None:
            return s1 + s2
        if candidate1 is not None and candidate2 is not None:
            return candidate1 if len(candidate1) <= len(candidate2) else candidate2
        if candidate1 is not None:
            return candidate1
        return candidate2

# Main section
for s1, s2 in [
                 ('aba', 'bab'),
                 ('aa', 'aaa'),
                 ('aaaxxxaaaa', 'aaaaxxxaa'),
                 ('xxx', 'yyy'),
                 ('m', 'azmvzfh'),
              ]:
    print(f's1 = {s1}')
    print(f's2 = {s2}')
    sol = Solution()
    r = sol.shortestSuperstring(s1, s2)
    print(f'r  = {r}')
    print('=======================')


















