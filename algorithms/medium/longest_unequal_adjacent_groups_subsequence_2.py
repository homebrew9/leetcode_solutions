from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # Using DP - Tabulation
        def check(s1, s2):
            if len(s1) != len(s2):
                return False
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        N = len(groups)
        dp = [1] * N
        prev = [-1] * N
        max_index = 0
        for i in range(1, N):
            for j in range(i):
                if check(words[i], words[j]) and dp[j] + 1 > dp[i] and groups[i] != groups[j]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i
        ans = []
        i = max_index
        while i >= 0:
            ans.append(words[i])
            i = prev[i]
        ans.reverse()
        return ans

# Main section
for words, groups in [
                        (['bab','dab','cab'], [1,2,2]),
                        (['a','b','c','d'], [1,2,3,4]),
                        (['bad','dc','bc','ccd','dd','da','cad','dba','aba'], [9,7,1,2,6,8,3,7,2]),
                     ]:
    print(f'words  = {words}')
    print(f'groups = {groups}')
    sol = Solution()
    r = sol.getWordsInLongestSubsequence(words, groups)
    print(f'r      = {r}')
    print('============================')



