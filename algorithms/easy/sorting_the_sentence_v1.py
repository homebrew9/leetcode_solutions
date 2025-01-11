#
# Using lambda and map
#
class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        arr.sort(key = lambda x: x[-1])
        return ' '.join(map(lambda x: x[:-1], arr))

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

