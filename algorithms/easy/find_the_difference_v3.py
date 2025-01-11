class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ssort = sorted(list(s))
        tsort = sorted(list(t))
        for a, b in zip(ssort, tsort):
            if a != b:
                return b
        return tsort[-1]

# Main section
sol = Solution()
for s, t in [
               ('abcd', 'abcde'),
               ('', 'y'),
               ('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyza'),
               ('aaaaa', 'aaaaaa'),
               ('aaaaa', 'baaaaa'),
               ('a', 'aa'),
            ]:
    print(f's = {s} ; t = {t}')
    r = sol.findTheDifference(s, t)
    print(f'r = {r}')
    print('======================')


