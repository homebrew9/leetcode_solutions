class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        '''
             a b c d
             c b a d (0,2)
             c d a b (1,3)
             a d c b (0,2)
             a b c d (1,3)
        '''
        arr = list(s1)
        for i, j in ((0,2), (1,3), (0,2), (1,3)):
            arr[i], arr[j] = arr[j], arr[i]
            if ''.join(arr) == s2:
                return True
        return False
    def canBeEqual_1(self, s1: str, s2: str) -> bool:
        return s1[2]+s1[1]+s1[0]+s1[3] == s2 or \
               s1[2]+s1[3]+s1[0]+s1[1] == s2 or \
               s1[0]+s1[3]+s1[2]+s1[1] == s2 or \
               s1 == s2

# Main section
for s1, s2 in [
                 ('abcd', 'cdab'),
                 ('abcd', 'dacb'),
              ]:
    print(f's1, s2 = {s1}, {s2}')
    sol = Solution()
    r = sol.canBeEqual(s1, s2)
    r1 = sol.canBeEqual_1(s1, s2)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===============================')



