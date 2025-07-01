class Solution:
    def possibleStringCount(self, word: str) -> int:
        N = len(word)
        res = 0
        left, right = 0, 0
        while right < N:
            if word[left] != word[right]:
                res += right - 1 - left
                left = right
            right += 1
        res += right - 1 - left
        return res + 1
    def possibleStringCount_1(self, word: str) -> int:
        N = len(word)
        res = 1
        for i in range(1, N):
            if word[i-1] == word[i]:
                res += 1
        return res

# Main section
for word in [
               'abbcccc',
               'abcd',
               'aaaa',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.possibleStringCount(word)
    r1 = sol.possibleStringCount_1(word)
    print(f'r    = {r}')
    print(f'r1   = {r1}')
    print('=======================')





