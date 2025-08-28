from collections import Counter

class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        cntr = Counter(s)
        res = ''
        for ch in s:
            if cntr[ch] < k:
                res += ch
        return res

    def filterCharacters_1(self, s: str, k: int) -> str:
        cntr = Counter(s)
        return ''.join([ch for ch in s if cntr[ch] < k])

# Main section
for s, k in [
               ('aadbbcccca', 3),
               ('xyz', 2),
               ('wamqlfwzkwnvzhnhooxgdeawvymvqhlrwyudlxacvoleetzarddydfxtxocfaeicueprvhtoefenznmhcwcbfpxwhpsjgidxtamb', 6)
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.filterCharacters(s, k)
    r1 = sol.filterCharacters_1(s, k)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('===================')




