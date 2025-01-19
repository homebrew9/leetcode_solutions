#
# Greedy algorithm
#
class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        N = len(arr)
        pfx = [None for _ in range(N)]
        val = -1
        ind = None
        for i in range(N-1, -1, -1):
            if int(arr[i]) > int(val):
                val = arr[i]
                ind = i
            pfx[i] = (val, ind)
        for i in range(N):
            if arr[i] < pfx[i][0]:
                j = pfx[i][1]
                arr[i], arr[j] = arr[j], arr[i]
                break
        return int(''.join(arr))

# Main section
for num in [
              2736,
              9973,
              1199,
              101,
              3003,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              50,
              100,
              101,
              2000,
              3000,
              47501924,
              48292900,
              64522746,
              29419857,
              20214541,
              58019819,
              87348316,
              4351640,
              92419996,
              23525951,
              123456,
              654321,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.maximumSwap(num)
    print(f'r   = {r}')
    print('=======================')


