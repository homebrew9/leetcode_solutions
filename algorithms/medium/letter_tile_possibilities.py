# Use Backtracking. Convert the string to a list and in each recursive call:
# 1) iterate through the list
# 2) pop a character, append it to string parameter
# 3) call recursive function
# 4) push back the character, remove it from string parameter (backtrack)
# 
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def solve(s, size):
            if len(s) == size:
                self.res.add(s)
                return
            for i in range(len(self.arr)):
                ch = self.arr.pop(i)
                s += ch
                solve(s, size)
                s = s[:-1]
                self.arr.insert(i, ch)
        self.arr = list(tiles)
        self.res = set()
        for n in range(1, len(tiles)+1):
            solve('', n)
        #print(self.res)
        return len(self.res)

# Main section
for tiles in [
                'AAB',
                'AAABBC',
                'V',
                'ABCDEFG',
                'XXXXXXX',
             ]:
    print(f'tiles = {tiles}')
    sol = Solution()
    r = sol.numTilePossibilities(tiles)
    print(f'r = {r}')
    print('==========================')

