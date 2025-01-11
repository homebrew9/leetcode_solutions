class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digitSum(n):
            return sum([int(i) for i in str(n)])

        if digitSum(n) <= target:
            return 0
        orig = n
        new_num = n
        i = 1
        p = n
        while n > 0:
            #print('p = %10d ; i = %5d ; new_num = %10d'%(p, i, new_num))
            if digitSum(new_num) <= target:
                break
            p = n // 10
            new_num = (p + 1) * (10**i)
            i += 1
            n = p

        print(f'new_num = {new_num} ; orig = {orig}')
        return (new_num - orig)

# Main section
for n, target in [
                    (16, 6),
                    (467, 6),
                    (1, 1),
                    (734504727, 10),
                    (8, 2),
                    (20, 2),
                    (201, 2),
                    (9, 1),
                    (5, 1),
                    (1, 2),
                 ]:
    print(f'n, target = {n}, {target}')
    sol = Solution()
    r = sol.makeIntegerBeautiful(n, target)
    print(f'r = {r}')
    print('================')


