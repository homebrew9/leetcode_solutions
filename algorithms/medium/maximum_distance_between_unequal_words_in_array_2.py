from typing import List

class Solution:
    def maxDistance(self, words: List[str]) -> int:
        N = len(words)
        for i in range(N):
            if words[i] != words[N - 1]:
                return max(N - i, i + 1)
        return 0

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
    print('====================')











