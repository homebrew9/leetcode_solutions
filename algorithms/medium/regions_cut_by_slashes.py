from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs(r, c, item):
            #print(r, c, item)
            #if not ((0 <= r < N) and (0 <= c < N)):
            #    return
            #if (r, c, item) not in does_exist:
            #    return
            #if (r, c, item) not in self.visited:
            #    self.visited.add((r, c, item))
            if item == 'SP':
                for h in sp_dir:
                    for k, v in h.items():
                        rnew = r + k[0]
                        cnew = c + k[1]
                        if (0 <= rnew < N) and (0 <= cnew < N):
                            for pat in v:
                                if (rnew, cnew, pat) in does_exist and (rnew, cnew, pat) not in self.visited:
                                    self.visited.add((rnew, cnew, pat))
                                    dfs(rnew, cnew, pat)
            elif item == 'BR':
                for h in br_dir:
                    for k, v in h.items():
                        rnew = r + k[0]
                        cnew = c + k[1]
                        if (0 <= rnew < N) and (0 <= cnew < N):
                            for pat in v:
                                if (rnew, cnew, pat) in does_exist and (rnew, cnew, pat) not in self.visited:
                                    self.visited.add((rnew, cnew, pat))
                                    dfs(rnew, cnew, pat)
            elif item == 'TL':
                for h in tl_dir:
                    for k, v in h.items():
                        rnew = r + k[0]
                        cnew = c + k[1]
                        if (0 <= rnew < N) and (0 <= cnew < N):
                            for pat in v:
                                if (rnew, cnew, pat) in does_exist and (rnew, cnew, pat) not in self.visited:
                                    self.visited.add((rnew, cnew, pat))
                                    dfs(rnew, cnew, pat)
            elif item == 'TR':
                for h in tr_dir:
                    for k, v in h.items():
                        rnew = r + k[0]
                        cnew = c + k[1]
                        if (0 <= rnew < N) and (0 <= cnew < N):
                            for pat in v:
                                if (rnew, cnew, pat) in does_exist and (rnew, cnew, pat) not in self.visited:
                                    self.visited.add((rnew, cnew, pat))
                                    dfs(rnew, cnew, pat)
            elif item == 'BL':
                for h in bl_dir:
                    for k, v in h.items():
                        rnew = r + k[0]
                        cnew = c + k[1]
                        if (0 <= rnew < N) and (0 <= cnew < N):
                            for pat in v:
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
        sp_dir = [{(0,1): ['SP','TL','BL']},
                  {(1,0): ['SP','TL','TR']},
                  {(0,-1): ['SP','TR','BR']},
                  {(-1,0): ['SP','BR','BL']},
                 ]
        br_dir = [{(0,1): ['SP','TL','BL']},
                  {(1,0): ['SP','TL','TR']},
                 ]
        tl_dir = [{(-1,0): ['SP','BR','BL']},
                  {(0,-1): ['SP','TR','BR']},
                 ]
        tr_dir = [{(-1,0): ['SP','BR','BL']},
                  {(0,1): ['SP','TL','BL']},
                 ]
        bl_dir = [{(1,0): ['SP','TL','TR']},
                  {(0,-1): ['SP','TR','BR']},
                 ]
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

