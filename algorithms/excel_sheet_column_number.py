class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 26
        hsh = dict()
        for i in range(base):
            hsh[chr(65+i)] = i + 1
        ret = 0
        place = 0
        for c in columnTitle[::-1]:
            place_value = base**place
            ret += int(hsh[c]) * place_value
            place += 1
        return ret

# Main section
sol = Solution()
for columnTitle in [
                      'A',
                      'AB',
                      'ZT',
                      'ZU',
                      'ZV',
                      'ZW',
                      'ZX',
                      'ZY',
                      'ZZ',
                      'AAA',
                      'AAB',
                      'AAC',
                      'AAD',
                      'AAE',
                      'ECW',
                      'FXSHRXW',
                  ]:
    print(f'columnTitle = {columnTitle}')
    r = sol.titleToNumber(columnTitle)
    print(f'r           = {r}')
    print('==================================')

