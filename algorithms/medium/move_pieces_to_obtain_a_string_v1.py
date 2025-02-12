#
# Without using Counter.
#
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        N = len(start)
        i, j = 0, 0
        while i < N and j < N:
            if start[i] == target[j] == '_':
                i += 1
                j += 1
            elif start[i] == '_':
                i += 1
            elif target[j] == '_':
                j += 1
            elif start[i] == target[j] == 'L' and i >= j:
                i += 1
                j += 1
            elif start[i] == target[j] == 'R' and i <= j:
                i += 1
                j += 1
            else:
                return False
        if i >= N:
            while j < N:
                if target[j] != '_':
                    return False
                j += 1
        if j >= N:
            while i < N:
                if start[i] != '_':
                    return False
                i += 1
        return True

# Main section
for start, target in [
                        ('_L__R__R_'     , 'L______RR'     ) ,
                        ('R_L_'          , '__LR'          ) ,
                        ('_R'            , 'R_'            ) ,
                        ('___L__R__'     , '_L_R_____'     ) ,
                        ('__R_L_L_R_LL'  , '___RLL___RLL'  ) ,
                        ('_L__R__R_'     , 'L______RR'     ) ,
                        ('__R_L__'       , '___RL__'       ) ,
                        ('__R_L__'       , '___R_L_'       ) ,
                        ('__L___LR__R__' , '_LL______R_R_' ) ,
                        ('_L__R__R_L'    , 'L______RR_'    ) ,
                        ('__L'           , 'L_L'           ) ,
                     ]:
    print(f'start  = {start}')
    print(f'target = {target}')
    sol = Solution()
    r = sol.canChange(start, target)
    print(f'r      = {r}')
    print('============================')



