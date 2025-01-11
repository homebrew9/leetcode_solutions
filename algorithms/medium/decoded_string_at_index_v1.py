class Solution:
    def decodeAtIndex(self, S, K):
        lens, n = [0], len(S)
        for c in S:
            if c.isdigit():
                lens.append(lens[-1]*int(c))
            else:
                lens.append(lens[-1] + 1)
        #print(f'\tlens = {lens}')
                
        for i in range(n, 0, -1):
            K %= lens[i]
            if K == 0 and S[i-1].isalpha():
                return S[i-1]

# Main section
for s, k in [
               ('leet2code3', 10),
               ('ha22', 5),
               ('a2345678999999999999999', 1),
               ('ab2cd3ef4', 79),
               ('ab2cd3ef4', 77),
               ('cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg', 480551547),
               ('a23', 6),
               ('vk6u5xhq9v', 554),
               ('hi2bob3', 18),
               ('hi2bob3', 3),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.decodeAtIndex(s, k)
    print(f'r = {r}')
    print('===================')


