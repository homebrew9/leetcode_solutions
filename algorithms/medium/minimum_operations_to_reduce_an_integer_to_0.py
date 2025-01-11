import math

class Solution:
    def minOperations(self, n: int) -> int:
        arr = list()
        def powerOfTwo(n, prev, sign, arr):
            #print(f'\tn, prev, arr = {n}, {prev}, {arr}')
            diff = abs(n - prev)
            p = round(math.log(diff)/math.log(2))
            if n > prev:
                curr = prev + 2**p
            else:
                curr = prev - 2**p
            if n == curr:
                arr.append(sign * 2**p)
                return arr
            if n > curr:
                arr.append(sign * 2**p)
                powerOfTwo(n, curr, 1, arr)
            elif n < curr:
                arr.append(sign * 2**p)
                powerOfTwo(n, curr, -1, arr)

        powerOfTwo(n, 0, 1, arr)
        #print(f'\tarr = {arr}')
        return len(arr)

# Main section
for n in [
            39,
            54,
            100000,
            1,
            99999,
            37839,
            883,
            9876,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.minOperations(n)
    print(f'r = {r}')
    print('==============')

