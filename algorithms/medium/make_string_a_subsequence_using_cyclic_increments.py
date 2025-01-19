class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def getPrevChar(ch):
            if 'b' <= ch <= 'z':
                return chr(ord(ch)-1)
            return 'z'
        N = len(str2)
        M = len(str1)
        if N > M:
            return False
        i = 0
        j = 0
        while i < N:
            ch = str2[i]
            found = False
            while j < M:
                if (str1[j] == ch or str1[j] == getPrevChar(ch)):
                    found = True
                    j += 1
                    break
                j += 1
            if j >= M and not found:
                return False
            i += 1
        if i >= N:
            return True
        else:
            return False

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


