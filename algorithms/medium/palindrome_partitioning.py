#
# Backtracking works fine, but the check for palindromes is done at the end.
# Is there a way to skip the arr formation if a substring is not a palindrome?
#
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Backtracking solution
        lst = list()
        def permute(s, arr):
            if len(s) == 0:
                valid = True
                for item in arr:
                    if item != item[::-1]:
                        valid = False
                        break
                if valid:
                    lst.append(arr)
            for i in range(len(s)):
                #print(i, s[:i+1], s[i+1:])
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
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.partition(s)
    print(f'r = {r}')
    print('==============')

