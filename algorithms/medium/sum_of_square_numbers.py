import math
class Solution:
    #def judgeSquareSum(self, c: int) -> bool:
    #    for i in range(1, c//2):
    #        low = i + 1
    #        high = c
    #        print(f'\tlow, high = {low}, {high}')
    #        while low <= high:
    #            mid = (low + high) // 2
    #            if i*i + mid*mid == c:
    #                return True
    #            elif i*i + mid*mid < c:
    #                low = mid + 1
    #            else:
    #                high = mid - 1
    #            print(f'\t\tlow, mid, high = {low}, {mid}, {high}')
    #    return False
    def judgeSquareSum(self, c: int) -> bool:
        i = 1
        while i*i < c:
            j = math.sqrt(c - i*i)
            if j == int(j):
                return True
            i += 1
        return False

# Main section
for c in [
            5,
            3,
            58,
            106,
            9938,
            10000,
            100000,
            123456,
            0,
            2147483647,
         ]:
    print(f'c = {c}')
    sol = Solution()
    r = sol.judgeSquareSum(c)
    print(f'r = {r}')
    print('==============')

