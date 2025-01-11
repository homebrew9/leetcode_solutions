import string

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        smallest = dict()
        for x in string.ascii_lowercase:
            smallest[x] = x

        def get_smallest(x):
            if smallest[x] != x:
                smallest[x] = get_smallest(smallest[x])
            return smallest[x]

        for a, b in zip(s1, s2):
            smaller = min(get_smallest(a), get_smallest(b))
            smallest[get_smallest(a)] = smaller
            smallest[get_smallest(b)] = smaller
            print(f'\t({a},{b}) : {["%s => %s"%(k, v) for k, v in smallest.items() if k != v]}')
        ans = list()
        for x in baseStr:
            ans.append(get_smallest(x))
        return ''.join(ans)

# Main section
for s1, s2, baseStr in [
                          ('leetcode', 'programs', 'sourcecode'),
                       ]:
    print(f's1, s2, baseStr = {s1}, {s2}, {baseStr}')
    sol = Solution()
    r = sol.smallestEquivalentString(s1, s2, baseStr)
    print(f'r = {r}')
    print('=============')

