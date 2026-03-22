class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        N = len(s)
        for i in range(N//2 + 1):
            if s[i] == s[N - i - 1]:
                return i
        return -1
    def firstMatchingIndex_1(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                return i
            i += 1
            j -= 1
        return -1

# Main section
for s in [
            'abcacbd',
            'abc',
            'abcdab',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.firstMatchingIndex(s)
    r1 = sol.firstMatchingIndex_1(s)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===============================')










