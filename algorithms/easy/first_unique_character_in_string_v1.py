class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Without using collections.Counter
        # We could probably use hsh only since key order is preserved
        # in Python 3.7+ ; an alternative is to use collections.OrderedDict
        hsh = dict()
        arr = list()
        for i, c in enumerate(s):
            if not c in hsh:
                hsh[c] = [1, i]
            else:
                hsh[c][0] += 1
            if not c in arr:
                arr.append(c)
            #print(f'hsh = {hsh}')
            #print(f'\tarr = {arr}')
            #print()
        for c in arr:
            if hsh[c][0] == 1:
                return hsh[c][1]
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


