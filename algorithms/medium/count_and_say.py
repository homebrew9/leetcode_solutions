class Solution:
    def countAndSay(self, n: int) -> str:
        def say(num):
            s = ''
            cnt = 0
            prev = None
            for digit in num:
                if prev is None:
                    cnt = 1
                elif digit == prev:
                    cnt += 1
                else:
                    s += str(cnt) + prev
                    cnt = 1
                prev = digit
                #print(f'\tdigit = {digit}, cnt = {cnt}, s = {s}')
            #print(f'digit = {digit}, cnt = {cnt}, s = {s}')
            s += str(cnt) + digit
            return s

        num = '1'
        for i in range(n-1):
            #print(f'i = {i}')
            ret = say(num)
            #print(ret)
            num = ret
        return num

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            10,
            15,
            20,
            25,
            30,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.countAndSay(n)
    print(f'r = {r}')
    print('=================')

