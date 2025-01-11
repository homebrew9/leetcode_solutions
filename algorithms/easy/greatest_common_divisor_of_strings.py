class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isDivisor(s, t):
            # Return True if string t is a divisor of s, False otherwise
            slen = len(s)
            tlen = len(t)
            i = 0
            while i < slen:
                if s[i:i+tlen] == t:
                    i += tlen
                else:
                    return False
            if i == slen:
                return True
            else:
                return False

        def gcdString(s, t):
            # Given that t is in s, return the gcd of s and t
            for i in range(len(t), 0, -1):
                chunk = t[:i]
                if isDivisor(s, chunk) and isDivisor(t, chunk):
                    return chunk
            return ''

        if str1 == str2:
            return str1
        elif str1 in str2:
            return gcdString(str2, str1)
        elif str2 in str1:
            return gcdString(str1, str2)
        else:
            return ''

# Main section
for str1, str2 in [
                     ('ABCABC', 'ABC'),
                     ('ABABAB', 'ABAB'),
                     ('LEET', 'CODE'),
                     ('ABABABAB', 'ABC'),
                     ('ABCDEF', 'ABC'),
                     ('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX'),
                  ]:
    print(f'str1, str2 = {str1}, {str2}')
    sol = Solution()
    r = sol.gcdOfStrings(str1, str2)
    print(f'r = {r}')
    print('======================')

