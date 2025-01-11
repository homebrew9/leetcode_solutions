#
# Very unusual way to solve the problem!
#

class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(s, t):
            #print(s, t)
            if t == '':
                if (s,t) in self.memo:
                    return self.memo[(s,t)]
                if s[0] == '0':
                    return 0
                if 1 <= int(s) <= 9:
                    self.memo[(s,t)] = 1
                    return self.memo[(s,t)]
                elif 10 <= int(s) <= 26:
                    self.memo[(s,t)] = 1 + dp(s[0], s[1])
                    return self.memo[(s,t)]
                elif int(s[:2]) > 26:
                    self.memo[(s,t)] = dp(s[:1], s[1:])
                    return self.memo[(s,t)]
                else:
                    self.memo[(s,t)] = dp(s[:1], s[1:]) + dp(s[:2], s[2:])
                    return self.memo[(s,t)]
            else:
                if 1 <= int(s) <= 26:
                    self.memo[(s,t)] = dp(t, '')
                    return self.memo[(s,t)]
        self.memo = dict()
        return dp(s, '')

# Main section
for s in [
            '33',
            '333',
            '3333',
            '11111122222222222111113333',
            '111111222222222221111133333333333111222',
            '12',
            '226',
            '111111111111111111111111111111111111111111111',
            '2125',
            '109',
            '111111222222222221111133333333333111222',
            '11111122222222222111113333',
            '12098928098098403984309809480382',
            '1212121215241524155214251212451',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.numDecodings(s)
    print(f'r = {r}')
    print('====================')

