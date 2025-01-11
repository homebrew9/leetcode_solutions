#
# Solution by Stefan Pochmann
# Ref: https://leetcode.com/problems/longest-absolute-file-path/discuss/86619/Simple-Python-solution
#
from typing import List

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth+1] = pathlen[depth] + len(name) + 1
        print(f'\tpathlen = {pathlen}')
        return maxlen

# Main section
for input in [
                'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext',
                'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
                'a',
                'dir\n\tsubdir1\n\tsubdir2\n\tsubdir3',
                'dir\n\tfile.ps\n\tsubdir2\n\tsubdir3',
                'dir\n\tfile0.ps\n\tsubdir1\n\tsubdir2\n\t\tfile1.txt\n\tsubdir3',
                'dir\n\tfile0.ps\n\tfile1.ps\n\tfile2.ps',
             ]:
    sol = Solution()
    print(f'input = \n{input}')
    print('~~~~~')
    r = sol.lengthLongestPath(input)
    print(f'r = {r}')
    print('==========================')


