#
# https://www.programiz.com/dsa/longest-common-subsequence
# Customized to return just the length. The original algo returns the LCS.
#
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs_algo(S1, S2, m, n):
            L = [[0 for x in range(n+1)] for x in range(m+1)]

            # Building the mtrix in bottom-up way
            for i in range(m+1):
                for j in range(n+1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif S1[i-1] == S2[j-1]:
                        L[i][j] = L[i-1][j-1] + 1
                    else:
                        L[i][j] = max(L[i-1][j], L[i][j-1])

            #print(f'\tL = {L}')
            return L[m][n]

        m = len(text1)
        n = len(text2)
        return lcs_algo(text1, text2, m, n)

# Main section
for text1, text2 in [
                       ('abcde', 'ace'),
                       ('abc', 'abc'),
                       ('abc', 'def'),
                       ('acadb', 'cbda'),
                    ]:
    print(f'text1, text2 = {text1}, {text2}')
    sol = Solution()
    r = sol.longestCommonSubsequence(text1, text2)
    print(f'r = {r}')
    print('===========================')

