class Solution:
    def isPalindrome(self, s: str) -> bool:
        isPalind = True
        lo = 0
        hi = len(s) - 1
        valid_chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        while True:
            if lo >= hi:
                break
            lc = s[lo]
            rc = s[hi]
            #print(f'\t>>> 0) lc, rc = {lc}, {rc}')
            #print(f'\t>>> 1) before while_1')
            while lc not in valid_chars:
                #print(f'\t\t>>> 1A) lo, lc = {lo}, {lc}')
                if lo < len(s)-1:
                    lo += 1
                    lc = s[lo]
                else:
                    #isPalind = False
                    break
            #print(f'\t>>> 2) before while_2')
            while rc not in valid_chars and hi >= 0:
                if hi > 0:
                    hi -= 1
                    rc = s[hi]
                else:
                    #isPalind = False
                    break
            lc = lc.lower()
            rc = rc.lower()
            #print(f'\t>>> 3) lc, rc = {lc}, {rc}')
            #print('')
            if lc in valid_chars and rc in valid_chars and lc != rc:
                isPalind = False
                break
            lo += 1
            hi -= 1
        return isPalind

# Main section
sol = Solution()
for s in [
              'A man, a plan, a canal: Panama',
              'race a car',
              ' ',
              'race-car',
              'hello911 abba 119olleh ',
              'malayalam',
              '--*!& redivider 1221 redivider #$%^+_{} redivider 1221 redivider !!@#()',
              'the woods are lovely, dark and deep',
              '.,',
              '~!@#$%^&  *()_+=-{}[]',
              '~',
              '~!@#$%^&W *()_+=-{}[]',
              '~!@#$%^&  *()_+=-{}[W',
              'W!@#$%^&  *()_+=-{}[]',
         ]:
    print(f's = [{s}]')
    r = sol.isPalindrome(s)
    print(f'r = {r}')
    print('================================')


