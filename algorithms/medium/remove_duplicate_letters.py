#
# Doesn't work for many inputs. Works only for trivial strings.
#
from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hsh = defaultdict(int)
        res = list()
        for ch in s:
            reorder_list = False
            if hsh[ch] == 0:
                res.append(ch)
            else:
                char_found = False
                for i, x in enumerate(res):
                    if char_found:
                        if x < ch or i == len(res) - 1:
                            reorder_list = True
                        break
                    elif x == ch:
                        char_found = True
            if reorder_list: 
                res.remove(ch)
                res.append(ch)
            hsh[ch] += 1
        return ''.join(res)

# Main section
for s in [
            'bcabc',
            #'cbacdcbc',
            #'aaaaabbbbbbccccccdddd',
            #'ddddaaaaabbbbbbccccccdddd',
            #'ddddaaaaabbbbbbcccccc',
            #'nxnvhwxpekeeumvlznromrrsvdooxcseythorvzqdjhtkygrezkwwjfgwuotmubxtzwxsplhupsubbqrdeftywyrdtwxfzvhzgaz',
            #'nxnvhwxpekeeumvlznromrr',  # Returns incorrect result "hwxpekuvlznomr"; correct result is "hwxpekumvlznor"
            #'nxnvhwxpekeeumvlznromr',   # Returns incorrect result "hwxpekuvlznomr"; correct result is "hwxpekumvlznor"
            #'nxnvhwxpekeeumvlznrom',    # Returns incorrect result "hwxpekuvlznrom"; correct result is "hwxpekumvlznro"
            #'nxnvhwxpekeeumvlznro',     # Returns correct result   "hwxpekumvlznro"
            'umvlznrom',                # Returns incorrect result "uvlznrom"; correct result is "umvlznro"
            'umvlznro',                 # Returns correct result "umvlznro"
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.removeDuplicateLetters(s)
    print(f'r = {r}')
    print('=====================')


