class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        n = 1
        arr1 = list()
        arr2 = list()
        while uniqueCnt1 > 0 or uniqueCnt2 > 0:
            print(f'\tn = {n}')
            if n % divisor1 != 0:
                print(f'\t\tin if...')
                if uniqueCnt1 > 0:
                    arr1.append(n)
                    uniqueCnt1 -= 1
                elif uniqueCnt2 > 0 and n % divisor2 != 0:
                    arr2.append(n)
                    uniqueCnt2 -= 1
                n += 1
            elif n % divisor2 != 0:
                print(f'\t\tin elif...')
                if uniqueCnt2 > 0:
                    arr2.append(n)
                    uniqueCnt2 -= 1
                elif uniqueCnt1 > 0 and n % divisor1 != 0:
                    arr1.append(n)
                    uniqueCnt1 -= 1
                n += 1
            else:
                print(f'\t\tin else...')
                n += 1
            print(f'\tarr1, arr2 = {arr1}, {arr2}')
            print('=====')
        return max(max(arr1), max(arr2))

# Main section
for divisor1, divisor2, uniqueCnt1, uniqueCnt2 in [
                #(2, 7, 1, 3),
                #(3, 5, 2, 1),
                #(2, 4, 8, 2),
                (12, 3, 2, 10),
             ]:
    print(f'divisor1, divisor2, uniqueCnt1, uniqueCnt2 = {divisor1}, {divisor2}, {uniqueCnt1}, {uniqueCnt2}')
    sol = Solution()
    r = sol.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2)
    print(f'r = {r}')
    print('================')

