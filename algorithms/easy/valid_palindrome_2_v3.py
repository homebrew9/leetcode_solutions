class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            return s == s[::-1]

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if isPalindrome(s[:i]+s[i+1:]):
                    return True
                elif isPalindrome(s[:j]+s[j+1:]):
                    return True
                else:
                    return False
            i += 1
            j -= 1
        return True

# Main section
for s in [
            'a',
            'aa',
            'ab',
            'aaa',
            'aba',
            'abca',
            'abc',
            'tebbem',
            'abcdefedcba',
            'abcddcba',
            'abcdedcxba',
            'abxcdedcba',
            'abxycdedcba',
            'abcdexfghijkjiyhgfedcba',
            'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.validPalindrome(s)
    print(f'r = {r}')
    print('===========================')

