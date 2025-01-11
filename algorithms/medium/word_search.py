from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def lookup(s, r, c, i, visited):
            print(f'\t\ts, (r, c), i, visited = {s}, {r}, {c}, {i}, {visited}')
            if s == word:
                return True
            #print(f'\t\t\t...before if # 2')
            if 0 <= r-1 < rows and 0 <= c < cols and not visited[r-1][c] and board[r-1][c] == word[i+1]:
                #print(f'\t\t\t...inside ({r-1}, {c})')
                #s += word[i+1]
                visited[r-1][c] = True
                ret = lookup(s+word[i+1], r-1, c, i+1, visited)
                if ret:
                    return True
                visited[r-1][c] = False
            #print(f'\t\t\t...before if # 3')
            if 0 <= r < rows and 0 <= c+1 < cols and not visited[r][c+1] and board[r][c+1] == word[i+1]:
                #print(f'\t\t\t...inside ({r}, {c+1})')
                #s += word[i+1]
                visited[r][c+1] = True
                ret = lookup(s+word[i+1], r, c+1, i+1, visited)
                if ret:
                    return True
                visited[r][c+1] = False
            #print(f'\t\t\t...before if # 4 => r+1, rows, c, cols, vis, wd = {r+1}, {rows}, {c}, {cols}, {visited}, {word[i+1]}')
            if 0 <= r+1 < rows and 0 <= c < cols and not visited[r+1][c] and board[r+1][c] == word[i+1]:
                #print(f'\t\t\t...inside ({r+1}, {c})')
                #s += word[i+1]
                visited[r+1][c] = True
                ret = lookup(s+word[i+1], r+1, c, i+1, visited)
                if ret:
                    return True
                visited[r+1][c] = False
            #print(f'\t\t\t...before if # 5')
            if 0 <= r < rows and 0 <= c-1 < cols and not visited[r][c-1] and board[r][c-1] == word[i+1]:
                #print(f'\t\t\t...inside ({r}, {c-1})')
                #s += word[i+1]
                visited[r][c-1] = True
                ret = lookup(s+word[i+1], r, c-1, i+1, visited)
                if ret:
                    return True
                visited[r][c-1] = False
            #print(f'\t\t\t...about to return')
            return False

        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                print(f'\t(r, c), ch = ({r}, {c}), {board[r][c]}')
                if board[r][c] == word[0]:
                    res = word[0]
                    pos = 0
                    visited[r][c] = True
                    ret = lookup(res, r, c, pos, visited)
                    #print(f'\tret = {ret}')
                    if ret:
                        return True
                    visited = [[False for _ in range(cols)] for _ in range(rows)]
        return False

# Main section
for board, word in [
                      ([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCCED'),
                      ([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'SEE'),
                      ([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'ABCB'),
                      ([['A','B','A','B'],['A','B','A','B'],['A','B','A','B']], 'BBBABAAABAAB'),
                      ([['A','B','A','B'],['A','B','A','B'],['A','B','A','B']], 'BABAAABABBAB'),
                      ([['A','B','C','D'],['E','F','G','H'],['I','J','K','L']], 'LKJIEABCDHGF'),
                      ([['C','A','A'],['A','A','A'],['B','C','D']], 'AAB'),
                      ([['A','B','C','E'],['S','F','E','S'],['A','D','E','E']], 'ABCEFSADEESE'),
                   ]:
    print(f'board, word = {board}, {word}')
    sol = Solution()
    r = sol.exist(board, word)
    print(f'r = {r}')
    print('==================')
     
