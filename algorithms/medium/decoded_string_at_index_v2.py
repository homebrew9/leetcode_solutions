class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        res = [0]
        count = 0
        for i, v in enumerate(s):
            if s[i].isalpha():
                count += 1
            else:
                count *= int(s[i])
            res.append(count)
        #print(f'\tres = {res}')
        N = len(res)
        for i in range(N-1, -1, -1):
            k %= res[i]
            if k == 0 and s[i-1].isalpha():
                return s[i-1]

# Main section
for s, k in [
               ('hi2bob3', 15),
               ('leet2code3', 10),
               ('ha22', 5),
               ('a2345678999999999999999', 1),
               ('cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg', 480551547),
               ('a23', 6),
               ('vk6u5xhq9v', 554),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.decodeAtIndex(s, k)
    print(f'r = {r}')
    print('===================')

