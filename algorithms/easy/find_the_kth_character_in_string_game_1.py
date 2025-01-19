#
# I used Brute Force. However, check the solutions that use bit count technique.
# How is bit count relevant here? Check solutions by lee215 or Spaulding.
#
class Solution:
    def kthCharacter(self, k: int) -> str:
        hsh = {chr(97+i) : chr(97+(i+1)%26) for i in range(26)}
        s = 'a'
        while len(s) < k:
            s += ''.join([hsh[ch] for ch in s])
        return s[k-1]

# Main section
for k in [
            1,
            2,
            5,
            10,
            97,
            105,
            359,
            473,
            500,
         ]:
    print(f'k = {k}')
    sol = Solution()
    r = sol.kthCharacter(k)
    print(f'r = {r}')
    print('===================')


