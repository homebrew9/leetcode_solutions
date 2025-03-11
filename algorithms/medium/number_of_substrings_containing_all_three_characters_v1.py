#
# Much shorter algorithm. Once we reach an index j such that s[i..j] is valid, then all indices from j to N-1
# end with valid substrings. Then reset i so that s[i..j] becomes invalid. Then back to sliding j again.
#
from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        hsh = defaultdict(int)
        res = 0
        i = 0
        for j in range(N):
            hsh[s[j]] += 1
            while len(hsh) == 3:
                res += N - j
                hsh[s[i]] -= 1
                if hsh[s[i]] == 0:
                    del hsh[s[i]]
                i += 1
        return res

# Main section
for s in [
            'bbacaab',
            'abcabc',
            'aaacb',
            'abc',
            'abbbaaa',
            'ababcbaacccccbbbabccbcaaccbaacaaccbababccccaaacabcccbbccbbaaabbcbacbcacbcbaccbabaabaacbabcabacbcbacb',
            'bcbcacbabaacbccbbcacbccbbbbcbcacbbaccbbabcabcaacbccacaacaccbbbbbabcbbaccccaaabacbaabbbabbcabccccacccccabcbcccbbccaccbcbaaacaaaaccbcaaacbbccaaabacbbbaacababcabbcbcbbabcababcbccbcccbccaabbcccbbaababccbabbbabaabbbaabccaaacbcccccabaccbabacbbbbaabccccbccaaabacaabaccaaabbbcccaacaaccbbbbbabcbacaaaaccbbacabaacaabbccabacaabbbbbaccbbcbaacabcbaaababbabbabbaabaccaaacaabcbbbbccaacacbabbaabcabbccbcbcbacccccbbacabaccaabccacaaacaccabbabacbcbcbacccbaabcbabacbbbccaccacccaacacabcaacbabccccbccbbbacbabbbbaabbbbccaababbbabaacaabbcababcccbbacbbcbaccccaccbcbabaaccccabababcabbbbacabababccbabbbbbcaaaccbbaccbaababacabbbacbcbbbccccbaaacaabcabbccccabcbacbcbacbacbccbccaacabcabbccacaaabbbbaaaabcbbbabccbbbccaabaabcbaaccbabccababbbbcacababcbaccabcbccccbbcaaaacbbbbbccbacacbcbbabcbcbacabaabcbacacabbaababccccccaabcaccbbccabbabbbcacaccaabacbcaccabcaabaaaccaacaaaaaaaabacacbbccacbbaacabcccacaccaabbbacabccbcccacacaaacabacaccccabbcaacaaccaaabbbacaacacaacacbccbacbbbbccbabbaacbcbbabbacacbcccaccaaacabcbbbaacaaccaccccccccbbccaaba',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.numberOfSubstrings(s)
    print(f'r = {r}')
    print('====================')

