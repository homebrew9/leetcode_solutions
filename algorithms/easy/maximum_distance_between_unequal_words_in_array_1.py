from typing import List

class Solution:
    def maxDistance(self, words: List[str]) -> int:
        N = len(words)
        res = 0
        for i in range(N):
            for j in range(i+1, N):
                if words[i] != words[j]:
                    res = max(res, j - i + 1)
        return res

# Main section
for words in [
                ['leetcode','leetcode','codeforces'],
                ['a','b','c','a','a'],
                ['z','z','z'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.maxDistance(words)
    print(f'r = {r}')
    print('==========================')






















