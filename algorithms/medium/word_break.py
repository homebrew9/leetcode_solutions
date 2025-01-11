from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache()
        def dfs(s):
            if len(s) == 0:
                return True
            chunk = ''
            for i, v in enumerate(s):
                chunk += v 
                if chunk in wordSet:
                    ret = dfs(s[i+1:])
                    if ret:
                        return True
            return False
        wordSet = set(wordDict)
        retval = dfs(s)
        if retval:
            return True
        else:
            return False

# Main section
for s, wordDict in [
                      ('catsandog', ['cats','dog','sand','and','cat']),
                      ('leetcode', ['leet','code']),
                      ('applepenapple', ['apple','pen']),
                      ('bduahcdbwzgscrtewdwfgrqrayzawxylbqasqqkprfeeddwtyg', ['bwsgmqq','dodnzsdigr','fd','unlrkerg','wk','vfxwrjhmkirjatnryy','evwulemdlos','chtwgmkwhziumzhcnqb','ezrgrsisazr','wfenzmexqgidvmlaiwni','oakrlrhk','ecmmpwtfy','mcbhrzruaurjezm','ixue','bcztxaddumpscv','wipdxsknbf','ztmdndxnknfkrwwtsl','ebzlbxxedooniltmput', 'dx','cqrryfnjjffuysxwx']),
                      ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa']),
                      ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ['a','aa','aaa','aaaa','aaaaa','aaaaaa','aaaaaaa','aaaaaaaa','aaaaaaaaa','aaaaaaaaaa']),
                   ]:
    print(f's, wordDict = {s}, {wordDict}')
    sol = Solution()
    r = sol.wordBreak(s, wordDict)
    print(f'r = {r}')
    print('=========================')


