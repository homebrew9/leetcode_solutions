from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hsh = defaultdict(int)
        for i, v in enumerate(s):
            hsh[v] = i
        seen = [0 for _ in range(26)]
        stack = list()
        orig = ord('a')
        for i, v in enumerate(s):
            if seen[ord(v) - orig] == 1:
                continue
            while len(stack) > 0 and stack[-1] > v and hsh[stack[-1]] > i:
                ch = stack.pop()
                seen[ord(ch) - orig] = 0
            stack.append(v)
            seen[ord(v) - orig] = 1
        res = ''
        while stack:
            res = stack.pop() + res
        return res

# Main section
for s in [
            'bcabc',
            'cbacdcbc',
            'aaaaabbbbbbccccccdddd',
            'ddddaaaaabbbbbbccccccdddd',
            'ddddaaaaabbbbbbcccccc',
            'nxnvhwxpekeeumvlznromrrsvdooxcseythorvzqdjhtkygrezkwwjfgwuotmubxtzwxsplhupsubbqrdeftywyrdtwxfzvhzgaz',
            'nxnvhwxpekeeumvlznromrr',  # Returns incorrect result "hwxpekuvlznomr"; correct result is "hwxpekumvlznor"
            'nxnvhwxpekeeumvlznromr',   # Returns incorrect result "hwxpekuvlznomr"; correct result is "hwxpekumvlznor"
            'nxnvhwxpekeeumvlznrom',    # Returns incorrect result "hwxpekuvlznrom"; correct result is "hwxpekumvlznro"
            'nxnvhwxpekeeumvlznro',     # Returns correct result   "hwxpekumvlznro"
            'umvlznrom',                # Returns incorrect result "uvlznrom"; correct result is "umvlznro"
            'umvlznro',                 # Returns correct result "umvlznro"
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.removeDuplicateLetters(s)
    print(f'r = {r}')
    print('=====================')



