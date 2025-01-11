class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return n
        arr = [[i, 1] for i in range(n)]
        k1 = k
        loss = 0
        res = None
        i = -1 
        found = False
        while True:
            i += 1
            ind = i % len(arr)
            if arr[ind][1] == 0:
                continue
            k1 -= 1
            if k1 == 0:
                arr[ind][1] = 0
                k1 = k
                loss += 1
                if loss == len(arr) - 1:
                    found = False
                    for i, v in enumerate(arr):
                        if v[1] == 1:
                            res = i + 1
                            found = True
                            break
            if found:
                return res

# Main section
for n, k in [
               (5, 1),
               (5, 2),
               (5, 3),
               (5, 4),
               (5, 5),
               (6, 5),
               (1, 1),
               (500, 274),
               (500, 1),
               (500, 97),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.findTheWinner(n, k)
    print(f'r = {r}')
    print('======================')


