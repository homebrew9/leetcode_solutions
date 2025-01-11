#
# Solution by lee215 - elegant logic but I think this logic cannot be
# generalized for any string.
#
class Solution:
    def addMinimum(self, word: str) -> int:
        k, prev = 0, 'z'
        for c in word:
            #print(f'\tc, prev, k, (c <= prev) = {c}, {prev}, {k}, {c <= prev}')
            if c <= prev:
                k += 1
            #k += c <= prev
            prev = c
        #print(f'final k = {k}')
        return k * 3 - len(word)

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


