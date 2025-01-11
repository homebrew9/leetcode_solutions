#
# This logic does not work for the last testcase!!
#
from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def isSpecialEquivalent(s, t):
            hsh1, hsh2 = {}, {}
            for i, ch in enumerate(s):
                if ch in hsh1:
                    hsh1[ch] += [i]
                else:
                    hsh1[ch] = [i]
            for i, ch in enumerate(t):
                if ch in hsh2:
                    hsh2[ch] += [i]
                else:
                    hsh2[ch] = [i]
            print(f'\ts, t = {s}, {t}')
            print(f'\thsh1 = {hsh1}')
            print(f'\thsh2 = {hsh2}')
            print(f'\t=====')
            if hsh1.keys() != hsh2.keys():
                return False
            for k in hsh1:
                if len(hsh1[k]) != len(hsh2[k]):
                    return False
                for a, b in zip(sorted(list(set(hsh1[k]) - set(hsh2[k]))), sorted(list(set(hsh2[k]) - set(hsh1[k])))):
                    if abs(a - b)%2 != 0:
                        return False
            return True

        ans = 0
        hsh = dict()
        for word in words:
            found_group = False
            for k in hsh:
                if isSpecialEquivalent(k, word):
                    hsh[k] += [word]
                    found_group = True
                    break
            if not found_group:
                hsh[word] = []
        print(f'hsh = {hsh}')
        ans = len(hsh)
        return ans

# Main section
for words in [
                #['abcd','cdab','cbad','xyzz','zzxy','zzyx'],
                #['abc','acb','bac','bca','cab','cba'],
                #['abcd','abdc','acbd','acdb','adbc','adcb','bacd','badc','bcad','bcda','bdac','bdca','cabd','cadb','cbad','cbda','cdab','cdba','dabc','dacb','dbac','dbca','dcab','dcba'],
                #['abcde','abced','abdce','abdec','abecd','abedc','acbde','acbed','acdbe','acdeb','acebd','acedb','adbce','adbec','adcbe','adceb','adebc','adecb','aebcd','aebdc','aecbd','aecdb','aedbc','aedcb','bacde','baced','badce','badec','baecd','baedc','bcade','bcaed','bcdae','bcdea','bcead','bceda','bdace','bdaec','bdcae','bdcea','bdeac','bdeca','beacd','beadc','becad','becda','bedac','bedca','cabde','cabed','cadbe','cadeb','caebd','caedb','cbade','cbaed','cbdae','cbdea','cbead','cbeda','cdabe','cdaeb','cdbae','cdbea','cdeab','cdeba','ceabd','ceadb','cebad','cebda','cedab','cedba','dabce','dabec','dacbe','daceb','daebc','daecb','dbace','dbaec','dbcae','dbcea','dbeac','dbeca','dcabe','dcaeb','dcbae','dcbea','dceab','dceba','deabc','deacb','debac','debca','decab','decba','eabcd','eabdc','eacbd','eacdb','eadbc','eadcb','ebacd','ebadc','ebcad','ebcda','ebdac','ebdca','ecabd','ecadb','ecbad','ecbda','ecdab','ecdba','edabc','edacb','edbac','edbca','edcab','edcba'],
                #['ababaa','aaabaa'],
                #['couxuxaubw','zsptcwcghr','kkntvvhbcc','nkhtcvvckb','crcwhspgzt'],
                ['fcrokswjnxglmjouwkht','shlgnfbgchiiytgxmamc','hynzlifgupwmwxbrbjdq','wkklgurjncmtfjoshxwo','kogsokwjnjrthlfxwcmu'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.numSpecialEquivGroups(words)
    print(f'r = {r}')
    print('=================')


