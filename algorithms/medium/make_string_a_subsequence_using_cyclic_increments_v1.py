import string
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        N = len(str1)
        M = len(str2)
        next_lst = string.ascii_lowercase[1:] + string.ascii_lowercase[0]
        i = 0
        for ch in str1:
            nextch = next_lst[ord(ch) - ord('a')]
            if i < M and str2[i] in (ch, nextch):
                i += 1
        return i == M

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


