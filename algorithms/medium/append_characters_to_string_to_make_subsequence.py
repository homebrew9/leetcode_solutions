class Solution:
    #def appendCharacters(self, s: str, t: str) -> int:
    #    i = 0
    #    j = 0
    #    while True:
    #        if i >= len(t):
    #            break
    #        ch = t[i]
    #        pos = s.find(ch, j)
    #        if pos == -1:
    #            break
    #        i += 1
    #        j = pos + 1
    #    return len(t) - i

    # Fantastic solution using "iter()" function
    def appendCharacters(self, s, t):
        it = iter(s)
        for i,c in enumerate(t):
            if c not in it:
                return len(t) - i
        return 0

# Main section
for s, t in [
               ['coaching', 'coding'],
               ['abcde', 'a'],
               ['z', 'abcde'],
            ]:
    print(f's, t = {s}, {t}')
    sol = Solution()
    r = sol.appendCharacters(s, t)
    print(f'r = {r}')
    print('===================')

