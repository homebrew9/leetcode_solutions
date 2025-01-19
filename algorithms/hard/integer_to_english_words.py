class Solution:
    def numberToWords(self, num: int) -> str:
        def one_digit(n):
            hsh = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                   6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
            return hsh[n]
        def two_digit(n):
            hsh1 = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                    20: 'twenty'}
            if 10 <= n <= 20:
                return hsh1[n]
            hsh = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
                   7: 'seventy', 8: 'eighty', 9: 'ninety'}
            p, q = divmod(n, 10)
            if q == 0:
                return hsh[p]
            else:
                return f'{hsh[p]} {one_digit(q)}'
        def three_digits(n):
            if n < 10:
                return one_digit(n)
            if n < 100:
                return two_digit(n)
            res = ''
            tag = 'hundred'
            p, q = divmod(n, 100)
            if q == 0:
                res = f'{one_digit(p)} {tag}'
            elif q < 10:
                res = f'{one_digit(p)} {tag} {one_digit(q)}'
            else:
                res = f'{one_digit(p)} {tag} {two_digit(q)}'
            return res
        if num == 0:
            return 'Zero'
        res = ''
        arr = list()
        while num > 0:
            p, q = divmod(num, 1000)
            arr = [q] + arr
            num = p
        triads = len(arr)
        hsh = {2: 'thousand', 3: 'million', 4: 'billion'}
        #print(arr, triads)
        for n in arr:
            if len(res) > 0 and n == 0:
                triads -= 1
                continue
            if triads > 1:
                res += f'{three_digits(n)} {hsh[triads]} '
            else:
                if (len(res) == 0) or (len(res) > 0 and n > 0):
                    res += f'{three_digits(n)} '
            triads -= 1
        return res.rstrip().title()

# Main section
for num in [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                30,
                57,
                78,
                98,
                99,
                100,
                101,
                102,
                399,
                400,
                401,
                467,
                500,
                990,
                991,
                992,
                998,
                999,
                1234,
                5678,
                12345,
                10001,
                10101,
                23456,
                20020,
                123456,
                1000,
                10000,
                100000,
                1234567,
                1000000,
                1000001,
                1000100,
                1000010,
                1100000,
                12345678,
                10000000,
                10000001,
                123456789,
                200001000,
                200000002,
                2147483647,
                1000000000,
                2000000000,
                2010304050,
                2147483646,
                2107000701,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.numberToWords(num)
    print(f'r = {r}')
    print('=====================')

