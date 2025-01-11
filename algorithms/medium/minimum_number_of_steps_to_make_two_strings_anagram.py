from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cntr = Counter(s)
        res = 0
        for ch in t:
            if ch in cntr and cntr[ch] > 0:
                cntr[ch] -= 1
        return sum(cntr.values())

# Main section
for s, t in [
               ('bab', 'aba'),
               ('leetcode', 'practice'),
               ('anagram', 'mangaar'),
               ('qyuskpyjpkxr', 'luwpczncxwwn'),
               ('qyuskpyjpkxrhflxrvfvzgiiygdbaiamdgbgqmxbojgbxyxzaz', 'luwpczncxwwnajnhmvbpvxstrhbdeoqvteeqcgaeeeskvgbctq'),
               ('fqjvtdnzyosbobxnmntxssndgwnkwtedbgjbbnybnbmmapmbax', 'qyarfzuizfjuyuwyjmqyjrefcqyhnlmdhtiimbxqdhjhdfclrt'),
            ]:
    print(f's, t = {s}, {t}')
    sol = Solution()
    r = sol.minSteps(s, t)
    print(f'r = {r}')
    print('=========================')

