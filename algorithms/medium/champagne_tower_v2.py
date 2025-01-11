class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[poured]]
        r = 0
        canOverflow = poured > 1
        while r < 99 and canOverflow:
            canOverflow = False
            tmp = [0 for _ in range(r+2)]
            for c in range(r+1):
                if tower[r][c] > 1:
                    flow_through = (tower[r][c] - 1)/2
                    tmp[c] += flow_through
                    tmp[c+1] += flow_through
                    tower[r][c] = 1
                    canOverflow = tmp[c] > 1 or tmp[c+1] > 1
            tower += [tmp]
            r += 1
        if r == 99:
            for c in range(r+1):
                if tower[r][c] > 1:
                    tower[r][c] = 1
        if query_row >= len(tower):
            return 0
        return tower[query_row][query_glass]

# Main section
for poured, query_row, query_glass in [
                                         (1, 1, 1),
                                         (2, 1, 1),
                                         (100000009, 33, 17),
                                         (13, 5, 0),
                                         (13, 5, 1),
                                         (13, 5, 2),
                                         (13, 5, 3),
                                         (13, 5, 4),
                                         (13, 5, 5),
                                         (1000000000, 99, 29),
                                         (48729327, 73, 21),
                                         (363, 29, 13),
                                         (13, 4, 1),
                                         (13, 93, 29),
                                      ]:
    print(f'poured, query_row, query_glass = {poured}, {query_row}, {query_glass}')
    sol = Solution()
    r = sol.champagneTower(poured, query_row, query_glass)
    print(f'r = {r}')
    print('=================')






