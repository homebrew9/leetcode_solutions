class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

# Main section
for s in [
            'Hello, my name is John',
            'Hello',
            'The quick brown fox jumps over the lazy dog',
            '',
            'a',
            'abc def   ghi   jkl   mno    pqr    stu   vw x y z',
            ' ',
            '     ',
            '     the quick brown    fox    ',
         ]:
    sol = Solution()
    print(f's = {s}')
    r = sol.countSegments(s)
    print(f'r = {r}')
    print('==========================')

