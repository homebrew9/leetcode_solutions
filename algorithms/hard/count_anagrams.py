from collections import Counter
import math

class Solution:
    def countAnagrams(self, s: str) -> int:
        def perm(word):
            size = len(word)
            cntr = Counter(word)
            res = math.factorial(size)
            for i, v in cntr.items():
                if v > 1:
                    res = res // math.factorial(v)
            return res
        
        cnt = 1
        MOD = 10**9 + 7
        for word in s.split():
            cnt = cnt * perm(word)
        return cnt % MOD

# Main section
for s in [
            'too hot',
            'aa',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.countAnagrams(s)
    print(f'r = {r}')
    print('========================')



