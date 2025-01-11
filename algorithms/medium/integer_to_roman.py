class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        hsh = {     1 :  'I',
                    4 : 'IV',
                    5 :  'V',
                    9 : 'IX',
                   10 :  'X',
                   40 : 'XL',
                   50 :  'L',
                   90 : 'XC',
                  100 :  'C',
                  400 : 'CD',
                  500 :  'D',
                  900 : 'CM',
                 1000 :  'M'
              }
        th, num = divmod(num, 1000)
        while th > 0:
            ans += hsh[1000]
            th -= 1
        hu, num = divmod(num, 100)
        if hu <= 3:
            while hu > 0:
                ans += hsh[100]
                hu -= 1
        elif hu == 4:
            ans += hsh[400]
        elif hu <= 8:
            ans += hsh[500]
            while hu > 5:
                ans += hsh[100]
                hu -= 1
        elif hu == 9:
            ans += hsh[900]
        tn, num = divmod(num, 10)
        if tn <= 3:
            while tn > 0:
                ans += hsh[10]
                tn -= 1
        elif tn == 4:
            ans += hsh[40]
        elif tn <= 8:
            ans += hsh[50]
            while tn > 5:
                ans += hsh[10]
                tn -= 1
        elif tn == 9:
            ans += hsh[90]
        if num <= 3:
            while num > 0:
                ans += hsh[1]
                num -= 1
        elif num == 4:
            ans += hsh[4]
        elif num <= 8:
            ans += hsh[5]
            while num > 5:
                ans += hsh[1]
                num -= 1
        elif num == 9:
            ans += hsh[9]
        return ans

# Main section
for num in [
                 1,
                 3,
                 9,
                10,
                11,
                58,
                67,
               101,
               178,
               567,
               687,
               999,
              1234,
              1994,
              3999,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.intToRoman(num)
    print(f'r = {r}')
    print('==================')

