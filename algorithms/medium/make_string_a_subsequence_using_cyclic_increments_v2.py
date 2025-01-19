#
# Yet another algorithm, which I think is more concise. Iterate through str2 and count how many characters
# we are able to match in str1. In the end, compare the count with the length of str2. This is very similar
# to v1 script, but we are doing the comparisons in reverse.
#

import string
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        N = len(str1)
        M = len(str2)
        prev_lst = string.ascii_lowercase[-1] + string.ascii_lowercase[:-1]
        i = 0
        cnt = 0
        for ch in str2:
            prev = prev_lst[ord(ch) - ord('a')]
            while i < N:
                if str1[i] in (ch, prev):
                    cnt += 1
                    i += 1
                    break
                i += 1
        return cnt == M

# Main section
for str1, str2 in [
                     ('abc', 'ad'),
                     ('zc', 'ad'),
                     ('ab', 'd'),
                     ('eao', 'ofa'),
                     ('abcd', 'abcd'),
                     ('abc', 'abcd'),
                     ('om', 'nm'),
                     ('kzmedxiatgvzgorszhjqaufcyubzbytulxapcftgcvftebctrboexicrgvrdtojkssxwvfekhdrpwsszdiejohnlrropztfvfaeu', 'tknymsfqha'),
                     ('dwjgcjbhmcfinhibqsmnkzhtmfkulqwyaoimnijeaygojdtskc', 'fbkzqjgsc'),
                     ('dwjgcjbhmcfinhibqsmnkzhtmfkulqwyaoimnijeaygojdtskc', 'gclarkgtd'),
                  ]:
    print(f'str1, str2 = {str1}, {str2}')
    sol = Solution()
    r = sol.canMakeSubsequence(str1, str2)
    print(f'r = {r}')
    print('=====================')


