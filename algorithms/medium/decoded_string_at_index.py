class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        count = 0
        letter = ''
        for i in range(len(s)):
            if s[i].isdigit():
                count *= int(s[i])
            else:
                count += 1
                letter = s[i]
            if count > k:
                break
            if count == k:
                return letter

        for j in range(i, -1, -1):
            if s[j].isdigit():
                count //= int(s[j])
            else:
                if k > count:
                    k %= count
                if k == 0 or count == k:
                    return s[j]
                count -= 1

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
               ('hi2bob3', 3),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.decodeAtIndex(s, k)
    print(f'r = {r}')
    print('===================')


