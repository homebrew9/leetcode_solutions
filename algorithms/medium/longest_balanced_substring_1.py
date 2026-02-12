from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        res = 0
        for i in range(N):
            hsh = defaultdict(int)
            for j in range(i, N):
                hsh[s[j]] += 1
                if len(set(hsh.values())) == 1:
                    res = max(res, j - i + 1)
        return res

# Main section
for s in [
            'abbac',
            'zzabccy',
            'aba',
            'x',
            'aa',
            'ab',
            'xyx',
            'brvlkzweeekxgjrcnmelakbfxtezecywcxpygbrdjsskeqqqduysenwjlwurayamkduxvwnfltvqmqbfgfgqsxrgxirtexjysvpzqpcvpkmuqtptruyhjttzwbckwiyhqy',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.longestBalanced(s)
    print(f'r = {r}')
    print('=================================================')
 



