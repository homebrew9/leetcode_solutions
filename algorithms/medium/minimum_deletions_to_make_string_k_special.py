from collections import defaultdict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1
        res = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            res = min(res, deleted)
        return res

# Main section
for word, k in [
                  ('aabcaba', 0),
                  ('dabdcbdcdcd', 2),
                  ('aaabaaa', 2),
               ]:
    print(f'word, k = {word}, {k}')
    sol = Solution()
    r = sol.minimumDeletions(word, k)
    print(f'r = {r}')
    print('=======================')

























