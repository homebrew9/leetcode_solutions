#
# Official solution
#

class Solution:
    def minMoves(self, rooks):
        # We simply have to determine how far off is each rook from its
        # "assigned" row and column. If we sort the rooks positions by row,
        # then the row index of each rook is its "assigned" row. The same
        # logic applies for the "assigned" column.
        min_moves = 0

        rooks.sort(key=lambda x: x[0])
        # Moves required to place rooks in each row
        for i in range(len(rooks)):
            min_moves += abs(i - rooks[i][0])

        rooks.sort(key=lambda x: x[1])
        # Moves required to place rooks in each column
        for i in range(len(rooks)):
            min_moves += abs(i - rooks[i][1])

        return min_moves

# Main section
for rooks in [
                [[0,0],[1,0],[1,1]],
                [[0,0],[0,1],[0,2],[0,3]],
                [[0,1],[1,2],[2,1],[3,3]],
                [[0,1],[3,2],[1,4],[0,2],[3,4]],
             ]:
    print(f'rooks = {rooks}')
    sol = Solution()
    r = sol.minMoves(rooks)
    print(f'r = {r}')
    print('====================')


