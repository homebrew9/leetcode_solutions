class Solution:
    def convertNumber(self, s: str) -> str:
        # One optimization trick is to check string chunks of lengths 5, 4, and 3 in that order.
        hsh = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
              }
        res = ''
        N = len(s)
        i = 0
        while i < N:
            if s[i:i+5] in hsh:
                res += hsh[s[i:i+5]]
                i += 5
            elif s[i:i+4] in hsh:
                res += hsh[s[i:i+4]]
                i += 4
            elif s[i:i+3] in hsh:
                res += hsh[s[i:i+3]]
                i += 3
            else:
                i += 1
        return res

# Main section
for s in [
            'onefourthree',
            'ninexsix',
            'zeero',
            'tw',
            'zero',
            'ffour',
            'jfone',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.convertNumber(s)
    print(f'r = {r}')
    print('===========================')






























