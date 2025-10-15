class Solution:
    def countDistinct(self, s: str) -> int:
        N = len(s)
        seen = set()
        res = 0
        for i in range(N):
            for j in range(i, N):
                curr = s[i:j+1]
                if curr not in seen:
                    seen.add(curr)
                    res += 1
        return res

# Main section
for s in [
            'aabbaba',
            'abcdefg',
            'mmhmgfrhcdaljokltlojzkbjnrkcmvevutgqtgvvkicxjvtiyakdncrfhraqguyaqvyfmbwgwpyamostfpvbtymxjigdqswoxfgo',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.countDistinct(s)
    print(f'r = {r}')
    print('=====================')




