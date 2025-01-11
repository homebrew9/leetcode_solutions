#
# Backtracking works for short strings <= 16 in length
#
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Backtracking solution
        lst = list()
        def permute(s, arr):
            if len(s) == 0:
                #print(f'\tarr = {arr}')
                lst.append(arr)
                return
            for i in range(len(s)):
                #print(i, s[:i+1], s[i+1:])
                chunk = s[:i+1]
                if chunk == chunk[::-1]:
                    permute(s[i+1:], arr + [s[:i+1]])
        arr = []
        permute(s, arr)
        return lst

# Main section
for s in [
            'aab',
            'a',
            'aaabbb',
            'abc',
            'aabbcc',
            'aabbccddeeffgghh',
            'aaaaaaaaaaaaaaaa',
            #'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.partition(s)
    print(f'r = {r}')
    print(f'len(r) = {len(r)}')
    print('==============')


