#
# Does not work for strings that have repeated characters!!
#
from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def isSpecialEquivalent(s, t):
            hsh1 = {ch:i for i, ch in enumerate(s)}
            hsh2 = {ch:i for i, ch in enumerate(t)}
            print(f'\thsh1 = {hsh1}')
            print(f'\thsh2 = {hsh2}')
            if hsh1.keys() != hsh2.keys():
                return False
            for k in hsh1:
                if abs(hsh1[k] - hsh2[k]) % 2 != 0:
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
        ans = len(hsh)
        return ans

# Main section
for words in [
                #['abcd','cdab','cbad','xyzz','zzxy','zzyx'],
                #['abc','acb','bac','bca','cab','cba'],
                #['abcd','abdc','acbd','acdb','adbc','adcb','bacd','badc','bcad','bcda','bdac','bdca','cabd','cadb','cbad','cbda','cdab','cdba','dabc','dacb','dbac','dbca','dcab','dcba'],
                #['abcde','abced','abdce','abdec','abecd','abedc','acbde','acbed','acdbe','acdeb','acebd','acedb','adbce','adbec','adcbe','adceb','adebc','adecb','aebcd','aebdc','aecbd','aecdb','aedbc','aedcb','bacde','baced','badce','badec','baecd','baedc','bcade','bcaed','bcdae','bcdea','bcead','bceda','bdace','bdaec','bdcae','bdcea','bdeac','bdeca','beacd','beadc','becad','becda','bedac','bedca','cabde','cabed','cadbe','cadeb','caebd','caedb','cbade','cbaed','cbdae','cbdea','cbead','cbeda','cdabe','cdaeb','cdbae','cdbea','cdeab','cdeba','ceabd','ceadb','cebad','cebda','cedab','cedba','dabce','dabec','dacbe','daceb','daebc','daecb','dbace','dbaec','dbcae','dbcea','dbeac','dbeca','dcabe','dcaeb','dcbae','dcbea','dceab','dceba','deabc','deacb','debac','debca','decab','decba','eabcd','eabdc','eacbd','eacdb','eadbc','eadcb','ebacd','ebadc','ebcad','ebcda','ebdac','ebdca','ecabd','ecadb','ecbad','ecbda','ecdab','ecdba','edabc','edacb','edbac','edbca','edcab','edcba'],
                ['ababaa','aaabaa'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.numSpecialEquivGroups(words)
    print(f'r = {r}')
    print('=================')

