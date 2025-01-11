from typing import List

class Solution:
    #def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    #    max_len = -1
    #    hsh = dict()
    #    for i, v in enumerate(s):
    #        if v in hsh:
    #            if i - hsh[v] - 1 > max_len:
    #                max_len = i - hsh[v] - 1
    #        hsh[v] = i
    #    print(hsh)
    #    return max_len

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_len = -1
        hsh = dict()
        for i, v in enumerate(s):
            if v in hsh:
                hsh[v].append(i)
            else:
                hsh[v] = [i]
        print(hsh)
        return max_len

# Main section
for s in [
            'mgntdygtxrvxjnwksqhxuxtrv',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.maxLengthBetweenEqualCharacters(s)
    print(f'r = {r}')
    print('===================')

