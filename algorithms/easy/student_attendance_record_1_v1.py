class Solution:
    def checkRecord(self, s: str) -> bool:
        # Let's try an algorithm that iterates through the characters.
        inBlock = False
        consecutiveLeaves = 0
        totalAbsences = 0
        for ch in s:
            if inBlock:
                if ch == 'L':
                    consecutiveLeaves += 1
                    if consecutiveLeaves >= 3:
                        return False
                else:
                    inBlock = False
                    consecutiveLeaves = 0
                    if ch == 'A':
                        totalAbsences += 1
                        if totalAbsences >= 2:
                            return False
            elif ch == 'L':
                if not inBlock:
                    inBlock = True
                consecutiveLeaves += 1
            elif ch == 'A':
                totalAbsences += 1
                if totalAbsences >= 2:
                    return False
        return True

# Main section
for s in [
            'PPALLP',
            'PPALLL',
            'PPPAPPPAPPPAPPPLLLPPP',
            'PPPPPPPPPPPPPPPPPPPPP',
            'APPPPLLPPPPPLLPPPPPPPPPPPPPPPPPPPPPPPPPPPA',
            'LALL',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.checkRecord(s)
    print(f'r = {r}')
    print('==========================')

