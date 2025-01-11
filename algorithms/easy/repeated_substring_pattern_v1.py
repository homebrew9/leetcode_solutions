class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]

# Main section
for s in [
            'abcdefghijabcdefghij',
            'abcdabcdabcbbcabcdabcd',
            'abcdabcdabcd',
            'abcabcabcabc',
            'a',
            'aa',
            'ab',
            'abc',
            'aba',
            'abcdefdefabc',
         ]:
    sol = Solution()
    print(f's = {s}')
    r = sol.repeatedSubstringPattern(s)
    print(f'r = {r}')
    print('==========================')


