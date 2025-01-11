from typing import List
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        hsh_p2s = dict()
        hsh_s2p = dict()
        for code, text in zip(pattern, s.split()):
            if code not in hsh_p2s and text not in hsh_s2p:
                hsh_p2s[code] = text
                hsh_s2p[text] = code
            elif code in hsh_p2s:
                if text not in hsh_s2p or hsh_s2p[text] != code:
                    return False
            elif text in hsh_s2p:
                if code not in hsh_p2s or hsh_p2s[code] != text:
                    return False
        return True

# Main section
sol = Solution()
for pattern, s in [
                     ['abba', 'dog cat cat dog'],
                     ['abba', 'dog cat cat fish'],
                     ['aaaa', 'dog cat cat dog'],
                     ['abba', 'dog dog dog dog'],
                     ['aba', 'dog cat cat'],
                     ['aaa', 'aa aa aa aa'],
                  ]:
    print(f'pattern = {pattern}')
    print(f's       = {s}')
    r = sol.wordPattern(pattern, s)
    print(f'r       = {r}')
    print('================')



