from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        N = len(s)
        if k > N:
            return 0
        cntr = Counter(s[:k])
        res = int(len(cntr) == k)
        for i in range(k, N):
            cntr[s[i-k]] -= 1
            if cntr[s[i-k]] == 0:
                del cntr[s[i-k]]
            cntr[s[i]] += 1
            res += len(cntr) == k
        return res

# Main section
for s, k in [
               ('havefunonleetcode', 5),
               ('home', 5),
               ('ddddgffejaebjajjcifibfbaegddbaegihhhgcjhdadfgfghjgchjefcadfgcdfbgacaiiabjibbjehecaihghjfeebceihciibc', 100)
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.numKLenSubstrNoRepeats(s, k)
    print(f'r = {r}')
    print('=======================')

