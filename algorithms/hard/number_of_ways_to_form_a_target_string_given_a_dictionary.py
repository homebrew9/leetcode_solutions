#
# This is a DP problem. The recursive DFS type algorithm works for small inputs, but throws TLE for
# the last algorithm. The Brute Force algorithm should be converted to a memoized solution.
# Another observation - adding the @cache decorator messes up the answers; my guess is that it is
# due to the inclusion of "total" in the parameter list. @cache can probably be used if only i and j
# are passed, but I can't seem to figure a way to do it.
#
from typing import List
from collections import defaultdict
from functools import cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        def solve(i, j, total):
            #print(i, j, total)
            if j >= M:
                self.res += total
                return
            for idx in range(i, N):
                if target[j] in hsh[idx]:
                    solve(idx+1, j+1, total * hsh[idx][target[j]])
        MOD = 10**9 + 7
        M = len(target)
        hsh = defaultdict(dict)
        for word in words:
            for i, v in enumerate(word):
                if v in hsh[i]:
                    hsh[i][v] += 1
                else:
                    hsh[i][v] = 1
        indices = sorted(list(hsh.keys()))
        N = len(indices)
        #print(hsh, indices, N)
        self.res = 0
        solve(0, 0, 1)
        return self.res % MOD

# Main section
for words, target in [
                        (['acca','bbbb','caca'], 'aba'),
                        (['abba','baab'], 'bab'),
                        (['aadd','ybee','zbcc'], 'abc'),
                        (['cbabddddbc','addbaacbbd','cccbacdccd','cdcaccacac','dddbacabbd','bdbdadbccb','ddadbacddd','bbccdddadd','dcabaccbbd','ddddcddadc','bdcaaaabdd','adacdcdcdd','cbaaadbdbb','bccbabcbab','accbdccadd','dcccaaddbc','cccccacabd','acacdbcbbc','dbbdbaccca','bdbddbddda','daabadbacb','baccdbaada','ccbabaabcb','dcaabccbbb','bcadddaacc','acddbbdccb','adbddbadab','dbbcdcbcdd','ddbabbadbb','bccbcbbbab','dabbbdbbcb','dacdabadbb','addcbbabab','bcbbccadda','abbcacadac','ccdadcaada','bcacdbccdb'], 'bcbbcccc'),
                        (['cabbaacaaaccaabbbbaccacbabbbcb','bbcabcbcccbcacbbbaacacaaabbbac','cbabcaacbcaaabbcbaabaababbacbc','aacabbbcaaccaabbaccacabccaacca','bbabbaabcaabccbbabccaaccbabcab','bcaccbbaaccaabcbabbacaccbbcbbb','cbbcbcaaaacacabbbabacbaabbabaa','cbbbbbbcccbabbacacacacccbbccca','bcbccbccacccacaababcbcbbacbbbc','ccacaabaaabbbacacbacbaaacbcaca','bacaaaabaabccbcbbaacacccabbbcb','bcbcbcabbccabacbcbcaccacbcaaab','babbbcccbbbbbaabbbacbbaabaabcc','baaaacaaacbbaacccababbaacccbcb','babbaaabaaccaabacbbbacbcbababa','cbacacbacaaacbaaaabacbbccccaca','bcbcaccaabacaacaaaccaabbcacaaa','cccbabccaabbcbccbbabaaacbacaaa','bbbcabacbbcabcbcaaccbcacacccca','ccccbbaababacbabcaacabaccbabaa','caaabccbcaaccabbcbcaacccbcacba','cccbcaacbabaacbaaabbbbcbbbbcbb','cababbcacbabcbaababcbcabbaabba','aaaacacaaccbacacbbbbccaabcccca','cbcaaaaabacbacaccbcbcbccaabaac','bcbbccbabaccabcccacbbaacbbcbba','cccbabbbcbbabccbbabbbbcaaccaab','acccacccaabbcaccbcaaccbababacc','bcacabaacccbbcbbacabbbbbcaaaab','cacccaacbcbccbabccabbcbabbcacc','aacabbabcaacbaaacaabcabcaccaab','cccacabacbabccbccaaaaabbcacbcc','cabaacacacaaabaacaabababccbaaa','caabaccaacccbaabcacbcbbabccabc','bcbbccbbaaacbaacbccbcbababcacb','bbabbcabcbbcababbbbccabaaccbca','cacbbbccabaaaaccacbcbabaabbcba','ccbcacbabababbbcbcabbcccaccbca','acccabcacbcbbcbccaccaacbabcaab','ccacaabcbbaabaaccbabcbacaaabaa','cbabbbbcabbbbcbccabaabccaccaca','acbbbbbccabacabcbbabcaacbbaacc','baaababbcabcacbbcbabacbcbaaabc','cabbcabcbbacaaaaacbcbbcacaccac'], 'acbaccacbbaaabbbabac'),
                     ]:
    print(f'words  = {words}')
    print(f'target = {target}')
    sol = Solution()
    r = sol.numWays(words, target)
    print(f'r  = {r}')
    print('=================')



