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

# Main section
for word in [
               'abbcccc',
               'abcd',
               'aaaa',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.possibleStringCount(word)
    print(f'r    = {r}')
    print('=======================')




