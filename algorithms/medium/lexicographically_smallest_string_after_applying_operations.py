class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def dfs(curr):
            if curr < res[0]:
                res[0] = curr
            
            # Operation 1: add 'a' to odd indices
            s1 = ''.join(
                str((int(ch) + a) % 10) if i % 2 == 1 else ch
                for i, ch in enumerate(curr)
            )
            if s1 not in visited:
                visited.add(s1)
                dfs(s1)
            
            # Operation 2: rotate right by b
            s2 = curr[-b:] + curr[:-b]
            if s2 not in visited:
                visited.add(s2)
                dfs(s2)

        visited = set()
        res = [s]  # mutable container to hold the best result
        visited.add(s)
        dfs(s)
        return res[0]

# Main section
for s, a, b in [
                  ('5525', 9, 2),
                  ('74', 5, 1),
                  ('0011', 4, 2),
                  ('3295765821', 3, 3),
                  ('496933170082640606557885531306', 7, 5),
               ]:
    print(f's, a, b = {s}, {a}, {b}')
    sol = Solution()
    r = sol.findLexSmallestString(s, a, b)
    print(f'r = {r}')
    print('=====================')








































