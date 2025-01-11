class Solution:
    def myAtoi(self, s: str) -> int:
        lower = -2**31
        upper = 2**31-1
        isNegative = False
        signed = False
        inNumber = False
        trueNumber = ''
        numTemplate = '1234567890'
        for i, c in enumerate(s):
            if not c in numTemplate:
                if not inNumber:
                    # We have are at the beginning of the string before any digit
                    # is seen; only spaces, '+' and '-' are allowed here
                    if c == '-':
                        if signed:
                            break
                        signed = True
                        isNegative = True
                    elif c == '+':
                        if signed:
                            break
                        signed = True
                        isNegative = False
                    elif c != ' ':
                        break
                else:
                    # We have started reading the number and encountered a non-digit
                    break
            else:
                if not inNumber:
                    if i > 0 and signed and not s[i-1] in ('+', '-'):
                        break
                    inNumber = True
                elif inNumber:
                    if not c in numTemplate:
                        break
                trueNumber += c
        if trueNumber == '':
            return 0
        if isNegative:
            trueNumber = '-' + trueNumber
        result = int(trueNumber)
        if result < lower:
            result = lower
        elif result > upper:
            result = upper
        return result

# Main section
sol = Solution()
for s in [
            '42',
            '    -42',
            '4193 with words',
            '   -4096 and some text',
            '       +99999999999999999999999999 3483993 and some more text',
            '       -99999999999999999999999999 3483993 and some more text',
            '-99999999999999999999999999 3483993 and some more text',
            '-999 3483993 xyz',
            '+999 3483993 xyz',
            '999 3483993 xyz',
            '-999.3483993 xyz',
            'words and 987',
            '--987',
            '++987',
            '- 987',
            '+ 987',
         ]:
    print(f's = {s}')
    r = sol.myAtoi(s)
    print(f'r = {r}')
    print('======================')

