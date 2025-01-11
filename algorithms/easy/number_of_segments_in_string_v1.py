class Solution:
    def countSegments(self, s: str) -> int:
        seg = 0
        in_seg = False
        for ch in s:
            if in_seg:
                if ch == ' ':
                    in_seg = False
            elif ch != ' ':
                seg += 1
                in_seg = True
        return seg

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


