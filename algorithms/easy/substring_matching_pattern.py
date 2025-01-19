#
# This one is tricky to solve character by character. The best intuition is to
# split the pattern into two parts and search for each separately. I used the
# Python regex in the contest though. That works for small inputs.
#
import re

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        i = p.find('*')
        left, right = p[:i], p[i+1:]
        if len(left) == 0 and len(right) == 0:
            return True
        if len(right) == 0:
            idx = s.find(left)
            return idx != -1
        if len(left) == 0:
            idx = s.find(right)
            return idx != -1
        idx = s.find(left)
        if idx == -1:
            return False
        idx1 = s.find(right, idx + len(left))
        if idx1 == -1:
            return False
        return True
    def hasMatch_1(self, s: str, p: str) -> bool:
        i = p.find('*')
        left, right = p[:i], p[i+1:]
        try:
            if len(left) == 0 and len(right) == 0:
                return True
            if len(right) == 0:
                idx = s.index(left)
            elif len(left) == 0:
                idx = s.index(right)
            else:
                idx = s.index(left)
                idx1 = s.index(right, idx + len(left))
            return True
        except:
            return False
    def hasMatch_2(self, s: str, p: str) -> bool:
        pattern = p
        pattern = pattern.replace('*', '.*')
        if pattern[0] == '.':
            pattern = '^' + pattern
        else:
            pattern = '^.*' + pattern
        if pattern[-1] == '*':
            pattern = pattern + '$'
        else:
            pattern = pattern + '.*$'
        #print(pattern)
        if re.search(pattern, s):
            return True
        else:
            return False

# Main section
for s, p, ans in [
                    ( 'leetcode'                        , 'ee*e'  , True  ),
                    ( 'car'                             , 'c*v'   , False ),
                    ( 'luck'                            , 'u*'    , True  ),
                    ( 'nrnrs'                           , '*nn'   , False ),
                    ( 'l'                               , '*'     , True  ),
                    ( 'jjj'                             , '*j'    , True  ),
                    ( 'abcabcabcabcabc'                 , 'ca*bc' , True  ),
                    ( 'abcabcabcabcabc'                 , 'a*c'   , True  ),
                    ( 'wwmwww'                          , 'wm*'   , True  ),
                    ( 'wmwmwmwmwmwmaaaaaaaaaaawxwxwxwx' , 'wm*we' , False ),
                    ( 'pep'                             , 'q*'    , False ),
                 ]:
    print(f's, p = {s}, {p}')
    sol = Solution()
    r = sol.hasMatch(s, p)
    print(f'r    = {r}')
    assert(r == ans)
    r1 = sol.hasMatch_1(s, p)
    print(f'r1   = {r1}')
    assert(r1 == ans)
    r2 = sol.hasMatch_2(s, p)
    print(f'r2   = {r2}')
    assert(r2 == ans)
    print('=======================')


