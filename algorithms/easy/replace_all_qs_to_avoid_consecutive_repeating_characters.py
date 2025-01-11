class Solution:
    def modifyString(self, s: str) -> str:
        def getNext(a=None, b=None):
            if (a is not None) and (b is not None):
                for ch in chars:
                    if ch != a and ch != b:
                        return ch
            elif a is None:
                for ch in chars:
                    if ch != b:
                        return ch
            elif b is None:
                for ch in chars:
                    if ch != a:
                        return ch
            else:
                return chars[0]

        t = list(s)
        chars = [chr(i+97) for i in range(26)]
        for i in range(0, len(t)):
            if t[i] == '?':
                if i == 0:
                    if i + 1 < len(t):
                        t[i] = getNext(t[i+1])
                    else:
                        t[i] = getNext()
                elif i == len(t) - 1:
                    t[i] = getNext(t[i-1])
                else:
                    t[i] = getNext(t[i-1], t[i+1])
        return ''.join(t)

# Main section
for s in [
            '?zs',
            'ubv?w',
            'a?c?e?g',
            'j?qg??b',
            '?',
            '??',
            '???',
            '????',
            '?????',
            '??????',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.modifyString(s)
    print(f'r = {r}')
    print('=======================')

