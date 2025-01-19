from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs(r, c, item):
            #print(r, c, item)
            if item == 'SP':
                for dr, dc in sp_dir:
                    rnew = r + dr
                    cnew = c + dc
                    if (0 <= rnew < N) and (0 <= cnew < N):
                        for pat in hsh_pat[(dr, dc)]:
                            if (rnew, cnew, pat) in does_exist and (rnew, cnew, pat) not in self.visited:
                                self.visited.add((rnew, cnew, pat))
                                dfs(rnew, cnew, pat)
            elif item == 'BR':
                for dr, dc in br_dir:
                    rnew = r + dr
                    cnew = c + dc
                    if (0 <= rnew < N) and (0 <= cnew < N):
                        for pat in hsh_pat[(dr, dc)]:
                            if (rnew, cnew, pat) in does_exist and (rnew, cnew, pat) not in self.visited:
                                self.visited.add((rnew, cnew, pat))
                                dfs(rnew, cnew, pat)
            elif item == 'TL':
                for dr, dc in tl_dir:
                    rnew = r + dr
                    cnew = c + dc
                    if (0 <= rnew < N) and (0 <= cnew < N):
                        for pat in hsh_pat[(dr, dc)]:
                            if (rnew, cnew, pat) in does_exist and (rnew, cnew, pat) not in self.visited:
                                self.visited.add((rnew, cnew, pat))
                                dfs(rnew, cnew, pat)
            elif item == 'TR':
                for dr, dc in tr_dir:
                    rnew = r + dr
                    cnew = c + dc
                    if (0 <= rnew < N) and (0 <= cnew < N):
                        for pat in hsh_pat[(dr, dc)]:
                            if (rnew, cnew, pat) in does_exist and (rnew, cnew, pat) not in self.visited:
                                self.visited.add((rnew, cnew, pat))
                                dfs(rnew, cnew, pat)
            elif item == 'BL':
                for dr, dc in bl_dir:
                    rnew = r + dr
                    cnew = c + dc
                    if (0 <= rnew < N) and (0 <= cnew < N):
                        for pat in hsh_pat[(dr, dc)]:
                            if (rnew, cnew, pat) in does_exist and (rnew, cnew, pat) not in self.visited:
                                self.visited.add((rnew, cnew, pat))
                                dfs(rnew, cnew, pat)

        N = len(grid)
        arr = [[None for _ in range(N)] for _ in range(N)]
        does_exist = set()
        r = 0
        for item in grid:
            for c, ch in enumerate(item):
                if ch == ' ':
                    arr[r][c] = ('SP',)
                    does_exist.add((r, c, 'SP'))
                elif ch == '/':
                    arr[r][c] = ('TL', 'BR')
                    does_exist.add((r, c, 'TL'))
                    does_exist.add((r, c, 'BR'))
                elif ch == '\\':
                    arr[r][c] = ('BL', 'TR')
                    does_exist.add((r, c, 'BL'))
                    does_exist.add((r, c, 'TR'))
            r += 1
        #print(arr)
        #print(does_exist)
        sp_dir = [(0,1), (1,0), (0,-1), (-1,0)]
        br_dir = [(0,1), (1,0)]
        tl_dir = [(-1,0), (0,-1)]
        tr_dir = [(-1,0), (0,1)]
        bl_dir = [(1,0), (0,-1)]
        hsh_pat = { (-1,0) : ['SP','BR','BL'],
                    (0,-1) : ['SP','TR','BR'],
                    (0,1)  : ['SP','TL','BL'],
                    (1,0)  : ['SP','TL','TR']
                  }
        self.visited = set()
        res = 0
        for r in range(N):
            for c in range(N):
                for item in arr[r][c]:
                    if (r, c, item) not in self.visited:
                        res += 1
                        self.visited.add((r, c, item))
                        dfs(r, c, item)
        return res

# Main section
for grid in [
               [' /','/ '],
               [' /','  '],
               ['/\\','\\/'],
               ['/\\/\\','\\/\\/','/\\/\\','\\/\\/'],
               ['/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/', '/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\', '\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/'],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.regionsBySlashes(grid)
    print(f'r = {r}')
    print('===========================')


