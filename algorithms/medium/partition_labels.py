from typing import List
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hsh = defaultdict(list)
        for i, v in enumerate(s):
            if v not in hsh:
                hsh[v] = [i, i]
            else:
                hsh[v][1] = i
        left, right = None, None
        in_block = False
        res = list()
        for i in range(len(s)):
            if not in_block:
                left = i
                right = hsh[s[i]][1]
                size = right - left + 1
                in_block = True
            elif hsh[s[i]][1] > right:
                right = hsh[s[i]][1]
                size = right - left + 1
            if i == right:
                in_block = False
                res.append(size)
                left, right = None, None
                in_block = False
        return res

# Main section
for s in [
            'ababcbacadefegdehijhklij',
            'eccbbbbdec',
            'abcdefghij',
            'ababababab',
            'aaaaaaaaaaaa',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.partitionLabels(s)
    print(f'r = {r}')
    print('========================')

