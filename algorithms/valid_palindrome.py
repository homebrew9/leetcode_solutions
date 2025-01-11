class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = list()
        for c in s:
            if 'a' <= c and c <= 'z':
                arr.append(c)
            if 'A' <= c and c <= 'Z':
                arr.append(c.lower())
            if '0' <= c and c <= '9':
                arr.append(c)
        return arr == arr[::-1]

# Main section
sol = Solution()
for s in [
              'A man, a plan, a canal: Panama',
              'race a car',
              ' ',
              'race-car',
              'hello911 abba 119olleh ',
              'malayalam',
              '--*!& redivider 1221 redivider #$%^+_{} redivider 1221 redivider !!@#()',
         ]:
    print(f's = [{s}]')
    r = sol.isPalindrome(s)
    print(f'r = {r}')
    print('================================')

