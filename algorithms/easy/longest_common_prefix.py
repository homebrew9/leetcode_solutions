from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for x in zip(*strs):
            if len(set(x)) == 1:
                res += x[0]
            else:
                break
        return res

# Main section
for strs in [
               ['flower','flow','flight'],
               ['dog','racecar','car'],
               ['aaa','aa','aaa'],
               ['a'],
               [''],
            ]:
    print(f'strs = {strs}')
    sol = Solution()
    r = sol.longestCommonPrefix(strs)
    print(f'r = {r}')
    print('===================')


