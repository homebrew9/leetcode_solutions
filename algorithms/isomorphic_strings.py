class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hsh_map = dict()
        for c1, c2 in zip(s, t):
            if c1 in hsh_map and hsh_map[c1] != c2:
                return False
            for k, v in hsh_map.items():
                if v == c2 and k != c1:
                    return False
            hsh_map[c1] = c2
        return True

# Main section
sol = Solution()
for s, t in [
               ("egg", "add"),
               ("foo", "bar"),
               ("paper", "title"),
               ("paper", "bible"),
               ("goga", "mamo"),
               ("badc", "baba"),
            ]:
    print(f's, t = {s}, {t}')
    r = sol.isIsomorphic(s, t)
    print(f'r = {r}')
    print('=================================')


