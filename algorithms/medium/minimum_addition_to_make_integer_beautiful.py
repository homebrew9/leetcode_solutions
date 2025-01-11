class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digitSum(n):
            return sum([int(i) for i in str(n)])

        if n == target:
            return 0
        if digitSum(n) <= target:
            return 0
        orig = n
        new_num = n
        i = 1
        while n > 0:
            p, q = divmod(n, 10)
            #if p != 0:
            new_num = (p + 1) * (10**i)
            #print('p = %10d ; q = %10d ; i = %5d ; new_num = %10d'%(p, q, i, new_num))
            if digitSum(new_num) <= target:
                break
            i += 1
            n = p

        #print(f'new_num = {new_num} ; orig = {orig}')
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

