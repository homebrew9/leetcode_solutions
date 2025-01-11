class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        n = num
        rev1 = 0
        while num > 0:
            num, r = divmod(num, 10)
            rev1 = 10*rev1 + r
        #print(f'rev1 = {rev1}')
        rev2 = 0
        while rev1 > 0:
            rev1, r = divmod(rev1, 10)
            rev2 = 10*rev2 + r
        #print(f'rev2 = {rev2}')
        return rev2 == n

# Main section
for num in [
              526,
              1800,
              0,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.isSameAfterReversals(num)
    print(f'r = {r}')
    print('=================')

