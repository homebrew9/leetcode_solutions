from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def fetch_subsequence(bit):
            arr = list()
            i = 0
            while i < N:
                if groups[i] == bit:
                    arr.append(words[i])
                    bit ^= 1
                i += 1
            return arr
        N = len(words)
        # Fetch the subsequences that starts with 0 and 1
        res1 = fetch_subsequence(0)
        res2 = fetch_subsequence(1)
        return res1 if len(res1) >= len(res2) else res2

# Main section
for words, groups in [
                        (['e','a','b'], [0,0,1]),
                        (['a','b','c','d'], [1,0,1,1]),
                     ]:
    print(f'words, groups = {words}, {groups}')
    sol = Solution()
    r = sol.getLongestSubsequence(words, groups)
    print(f'r  = {r}')
    print('============================')
















