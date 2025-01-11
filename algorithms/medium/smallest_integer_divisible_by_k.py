class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = '1' * len(str(k))
        hsh = dict()
        while True:
            print(f'\tn, hsh = {n}, {hsh}')
            if int(n) % k == 0:
                break
            r = int(n) % k
            if r in hsh:
                return -1
            hsh[r] = 1
            n += '1'
        return len(n)

# Main section
for k in [
            #1,
            #2,
            #3,
            #101,
            #250,
            #41,
            #271,
            #37,
            #1111,
            19927,
         ]:
    print(f'k = {k}')
    sol = Solution()
    r = sol.smallestRepunitDivByK(k)
    print(f'r = {r}')
    print('===================')

