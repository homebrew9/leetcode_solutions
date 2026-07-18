from collections import Counter

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        cntr = Counter(s)
        res = ''
        if y in s:
            res += y * cntr[y]
        if x in s:
            res += x * cntr[x]
        for k, v in cntr.items():
            if k != x and k != y:
                res += k * v
        return res
    def rearrangeString_1(self, s: str, x: str, y: str) -> str:
        return ''.join(sorted(s)) if y < x else ''.join(reversed(sorted(s)))
    def rearrangeString_2(self, s: str, x: str, y: str) -> str:
        return ''.join(sorted(s, reverse=y > x))
    def rearrangeString_3(self, s: str, x: str, y: str) -> str:
        arr = list(s)
        if x in s and y in s:
            xcount, ycount = 0, 0
            for i, v in enumerate(arr):
                if v == x:
                    xcount += 1
                elif v == y:
                    ycount += 1
            for i, v in enumerate(arr):
                if v == x or v == y:
                    if ycount > 0:
                        arr[i] = y
                        ycount -= 1
                    else:
                        arr[i] = x
                        xcount -= 1
                else:
                    arr[i] = v
            return ''.join(arr)
        return s

# Main section
for s, x, y in [
                  ('aabc', 'a', 'c'),
                  ('dcab', 'd', 'b'),
                  ('axe', 'o', 'x'),
                  ('rakbcfscthxjhzwotvsxxvhqrmzjutssjfcmtaqchnzqvmsjdhnjdnnhpvbqlzxyqwcnuigirhgafkodzouajzgqfpjthhlgvfoi', 'a', 'z'),
               ]:
    print(f's, x, y = {s}, {x}, {y}')
    sol = Solution()
    r  = sol.rearrangeString(s, x, y)
    r1 = sol.rearrangeString_1(s, x, y)
    r2 = sol.rearrangeString_2(s, x, y)
    r3 = sol.rearrangeString_3(s, x, y)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print(f'r3 = {r3}')
    print('===================================')












