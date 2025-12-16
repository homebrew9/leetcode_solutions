class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = set()
        res = 0
        for ch in s:
            if ch not in seen:
                res += 1
                seen.add(ch)
        return res
    def maxDistinct_1(self, s: str) -> int:
        return len(set(s))

# Main section
for s in [
            'abab',
            'abcd',
            'aaaa',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.maxDistinct(s)
    r1 = sol.maxDistinct(s)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===========================')










