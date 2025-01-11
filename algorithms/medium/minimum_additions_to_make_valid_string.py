class Solution:
    def addMinimum(self, word: str) -> int:
        N = len(word)
        ref = 'abc' * N
        i, j = 0, 0
        mod = None
        res = 0
        while i < N:
            if word[i] != ref[j]:
                res += 1
            else:
                i += 1
            j += 1
            mod = j % 3
        if mod > 0:
            res += (3 - mod)
        return res

# Main section
for word in [
               'b',
               'aa',
               'bb',
               'ca',
               'ac',
               'cba',
               'aaa',
               'abc',
               'acc',
               'abcabc',
               'aaaaabbbbbcccccabababababc',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.addMinimum(word)
    print(f'r = {r}')
    print('==================')

