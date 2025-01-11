#
# Leonardo Rossi solution with some customizations.
#
from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache()
        def check(a, b, c):
            #print(f'\ta, b, c = {a}, {b}, {c}')
            if a == len(s1) and b == len(s2) and c == len(s3):
                # We matched everything: interleaving completed
                return True
            # We use string[i:i+1] to handle all strings, including empty
            # strings, in one shot. If a string is empty, then string[i:i+1]
            # is also empty.
            sa = s1[a:a+1]
            sb = s2[b:b+1]
            sc = s3[c:c+1]
            #print(f'\t\tsa, sb, sc = [{sa}], [{sb}], [{sc}]')
            if sa == sb == sc:
                # We do not know which way to continue; try both options
                return check(a+1, b, c+1) or check(a, b+1, c+1)
            if sa == sc:
                # Consume the first character of s1
                return check(a+1, b, c+1)
            elif sb == sc:
                # Consume the first character of s2
                return check(a, b+1, c+1)
            else:
                # First character of s3 matches neither that of s1 nor s2
                return False
        if len(s3) != len(s1) + len(s2):
            return False
        return check(0, 0, 0)

# Main section
for s1, s2, s3 in [
                     ('aabcc', 'dbbca', 'aadbbcbcac'),
                     ('aabcc', 'dbbca', 'aadbbbaccc'),
                     ('', '', ''),
                     ('', 'b', 'b'),
                     ('a', 'b', 'a'),
                     ('bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa', 'babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab', 'babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab'),
                  ]:
    print(f's1, s2, s3 = {s1}, {s2}, {s3}')
    sol = Solution()
    r = sol.isInterleave(s1, s2, s3)
    print(f'r = {r}')
    print('=====================')


