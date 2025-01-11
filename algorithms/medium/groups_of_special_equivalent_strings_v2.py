from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        # Since we can "move" characters at odd indexes throughout the string, if
        # we extract a list of characters at odd indexes and sort them, then that
        # should be the same for equivalent strings. Same logic for chars at even
        # indexes. The code below uses that logic to generate a set of unique
        # "odd-even-sort-strings" from all words.
        st = set()
        for word in words:
            sort_even = ''.join(sorted(word[0::2]))
            sort_odd  = ''.join(sorted(word[1::2]))
            #print(f'\tword, sort_even, sort_odd = {word}, {sort_even}, {sort_odd}')
            st.add(sort_even+sort_odd)
        return len(st)

# Main section
for words in [
                ['abcd','cdab','cbad','xyzz','zzxy','zzyx'],
                ['abc','acb','bac','bca','cab','cba'],
                ['abcd','abdc','acbd','acdb','adbc','adcb','bacd','badc','bcad','bcda','bdac','bdca','cabd','cadb','cbad','cbda','cdab','cdba','dabc','dacb','dbac','dbca','dcab','dcba'],
                ['abcde','abced','abdce','abdec','abecd','abedc','acbde','acbed','acdbe','acdeb','acebd','acedb','adbce','adbec','adcbe','adceb','adebc','adecb','aebcd','aebdc','aecbd','aecdb','aedbc','aedcb','bacde','baced','badce','badec','baecd','baedc','bcade','bcaed','bcdae','bcdea','bcead','bceda','bdace','bdaec','bdcae','bdcea','bdeac','bdeca','beacd','beadc','becad','becda','bedac','bedca','cabde','cabed','cadbe','cadeb','caebd','caedb','cbade','cbaed','cbdae','cbdea','cbead','cbeda','cdabe','cdaeb','cdbae','cdbea','cdeab','cdeba','ceabd','ceadb','cebad','cebda','cedab','cedba','dabce','dabec','dacbe','daceb','daebc','daecb','dbace','dbaec','dbcae','dbcea','dbeac','dbeca','dcabe','dcaeb','dcbae','dcbea','dceab','dceba','deabc','deacb','debac','debca','decab','decba','eabcd','eabdc','eacbd','eacdb','eadbc','eadcb','ebacd','ebadc','ebcad','ebcda','ebdac','ebdca','ecabd','ecadb','ecbad','ecbda','ecdab','ecdba','edabc','edacb','edbac','edbca','edcab','edcba'],
                ['ababaa','aaabaa'],
                ['couxuxaubw','zsptcwcghr','kkntvvhbcc','nkhtcvvckb','crcwhspgzt'],
                ['fcrokswjnxglmjouwkht','shlgnfbgchiiytgxmamc','hynzlifgupwmwxbrbjdq','wkklgurjncmtfjoshxwo','kogsokwjnjrthlfxwcmu'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.numSpecialEquivGroups(words)
    print(f'r = {r}')
    print('=================')

