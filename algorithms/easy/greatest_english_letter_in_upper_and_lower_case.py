class Solution:
    def greatestLetter(self, s: str) -> str:
        lchars = [0 for i in range(97, 123)]
        uchars = [0 for i in range(65, 91)]
        max_index = -1
        for ch in s:
            if 65 <= ord(ch) <= 90:
                ind = ord(ch) - 65
                uchars[ind] += 1
                if lchars[ind] > 0:
                    max_index = max(max_index, ind)
            elif 97 <= ord(ch) <= 122:
                ind = ord(ch) - 97
                lchars[ind] += 1
                if uchars[ind] > 0:
                    max_index = max(max_index, ind)
        if max_index < 0:
            return ''
        else:
            return chr(max_index + 65)

# Main section
for s in [
            'lEeTcOdE',
            'arRAzFif',
            'AbCdEfGhIjK',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.greatestLetter(s)
    print(f'r = {r}')
    print('==========================')

