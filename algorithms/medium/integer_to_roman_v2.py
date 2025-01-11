#
# Add the code to handle 40/400/90/900 etc. Reduce the hash length.
#
class Solution:
    def intToRoman(self, num: int) -> str:
        def addRomanLetters(n, mult):
            global ans, hsh
            if n <= 3:
                while n > 0:
                    ans += hsh[mult]
                    n -= 1
            elif n == 4:
                ans += hsh[mult] + hsh[5*mult]
            elif n <= 8:
                ans += hsh[5*mult]
                while n > 5:
                    ans += hsh[mult]
                    n -= 1
            elif n == 9:
                ans += hsh[mult] + hsh[10*mult]

        global ans, hsh
        ans = ''
        hsh = {     1 :  'I',
                    5 :  'V',
                   10 :  'X',
                   50 :  'L',
                  100 :  'C',
                  500 :  'D',
                 1000 :  'M'
              }
        th, num = divmod(num, 1000)
        while th > 0:
            ans += hsh[1000]
            th -= 1
        hu, num = divmod(num, 100)
        addRomanLetters(hu, 100)
        tn, num = divmod(num, 10)
        addRomanLetters(tn, 10)
        addRomanLetters(num, 1)
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



