class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        N = len(target)
        M = len(source)
        res = 0
        j = 0
        while j < N:
            matched = False
            i = 0
            while i < M and j < N:
                if source[i] == target[j]:
                    j += 1
                    matched = True
                i += 1
            if not matched:
                return -1
            res += 1
        return res

# Main section
for source, target in [
                         ('abc', 'abcbc'),
                         ('abc', 'acdbc'),
                         ('xyz', 'xzyxz'),
                      ]:
    print(f'source, target = {source}, {target}')
    sol = Solution()
    r = sol.shortestWay(source, target)
    print(f'r = {r}')
    print('========================')

