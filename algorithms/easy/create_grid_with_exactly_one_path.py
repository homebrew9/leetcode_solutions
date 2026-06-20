class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        rows, cols = m, n
        res = list()
        res.append('.' * cols)
        for r in range(1, rows):
            tmp = '#' * (cols - 1) + '.'
            res.append(tmp)
        return res

# Main section
for m, n in [
               (2, 3),
               (3, 3),
               (1, 4),
               (5, 1),
            ]:
    print(f'm, n = {m}, {n}')
    sol = Solution()
    r = sol.createGrid(m, n)
    print(f'r = {r}')
    print('===================================')











