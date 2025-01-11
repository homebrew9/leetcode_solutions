from typing import List

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        arr = input.split('\n')
        hsh = dict()
        maxLen = 0
        for item in arr:
            print(f'\titem = {item}')
            level = item.count('\t')
            itype = 'd' if item.find('.') < 0 else 'f'
            item = item.replace('\t','')
            ilen = len(item)
            if level > 0:
                ilen += hsh[level-1][-1][1] + 1
            if level not in hsh:
                hsh[level] = [(item, ilen, itype)]
            else:
                hsh[level] += [(item, ilen, itype)]
            if itype == 'f':
                maxLen = max(maxLen, ilen)
        return maxLen
        
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

