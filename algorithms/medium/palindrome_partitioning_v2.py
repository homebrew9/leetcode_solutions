#
# Backtracking + DP - Even this is not fast enough for the last test case.
#
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        #print(f'\tdp = {dp}')
        result = list()
        currentList = list()

        def dfs(result, s, start, currentList, dp):
            #print(f'\t\tcurrentList, dp = {currentList}, {dp}')
            if start >= len(s):
                result.append(list(currentList))
                #print(f'\t\t\tresult = {result}')
            for end in range(start, len(s)):
                if s[start] == s[end] and (end - start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True
                    currentList.append(s[start:end+1])
                    dfs(result, s, end+1, currentList, dp)
                    currentList.pop()

        dfs(result, s, 0, currentList, dp)
        #print(dp)
        return result

# Main section
for s in [
            'aab',
            'a',
            'aaabbb',
            'abc',
            'aabbcc',
            'aaa',
            'aabbccddeeffgghh',
            'aaaaaaaaaaaaaaaa',
            #'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.partition(s)
    print(f'r = {r}')
    #print(f'len(r) = {len(r)}')
    print('==============')



