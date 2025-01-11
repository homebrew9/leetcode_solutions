class Solution:
    def smallestString(self, s: str) -> str:
        # If the string consists only of 'a' then the last
        # 'a' must be converted to 'z'
        if len(set(s)) == 1 and s[0] == 'a':
            return s[:-1] + 'z'
        # Otherwise:
        # - skip any initial contiguous string of 'a' characters
        # - start updating the non 'a' characters
        # - stop when 'a' is seen again
        in_block = False
        res = ''
        for i, ch in enumerate(s):
            if in_block:
                if ch == 'a':
                    res += s[i:]
                    break
                else:
                    res += chr(ord(ch)-1)
            elif ch == 'a':
                res += ch
                continue
            else:
                in_block = True
                res += chr(ord(ch)-1)
        return res

# Main section
for s in [
            'cbabc',
            'acbbc',
            'leetcode',
            'aaaxaaa',
            'aaaxayz',
            'xaaa',
            'xayz',
            'a',
            'aa',
            'aaa',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.smallestString(s)
    print(f'r = {r}')
    print('===================')



