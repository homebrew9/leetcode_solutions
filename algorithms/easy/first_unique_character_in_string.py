from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cntr = Counter(s)
        for i, c in enumerate(s):
            if cntr[c] == 1:
                return i
        return -1

# Main section
sol = Solution()
for s in [
            "loveleetcode",
            "aabb",
            "thequickbrownfoxjumpsoverthelazydog",
            "aaaaaaaaaaaaaaaaaa",
            "abcdefabcdefg",
            "aadadaad",
         ]:
    print(f's = {s}')
    r = sol.firstUniqChar(s)
    print(f'r = {r}')
    print('======================')

