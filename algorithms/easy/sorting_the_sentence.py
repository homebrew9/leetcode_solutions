class Solution:
    def sortSentence(self, s: str) -> str:
        hsh = {i[-1]: i[:-1] for i in s.split()}
        t = ''
        for k in sorted(hsh):
            t += hsh[k] + ' '
        return t.rstrip()

# Main section
for s in [
            'is2 sentence4 This1 a3',
            'Myself2 Me1 I4 and3',
         ]: 
    print(f's = {s}')
    sol = Solution()
    r = sol.sortSentence(s)
    print(f'r = {r}')
    print('=========================')

