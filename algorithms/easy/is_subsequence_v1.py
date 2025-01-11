# This solution does not work for s = 'abcdef', t = 'fedcba' because the
# deletion in t occurs from "right-to-left". The deletion should occur
# from left to right. So unless we pass the index to the recursive function,
# I can't see how we can solve this problem. Even passing the index may
# not work! Let me see if it can work with an inner function.
#
# I got stuck; the following link helped!
# Ref: https://leetcode.com/problems/is-subsequence/discuss/1811177/C%2B%2B-oror-Recursion-and-Two-pointer
#

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Inline function that iterates through the strings and determines
        # the number of characters of s that were found in t, going right
        # to left.
        def findMatchCount(s, t, m, n):
            #print(f's, t, m, n = {s}, {t}, {m}, {n}')
            # If we have reached the leftmost position in either string,
            # then stop and return 0
            if m == 0 or n == 0:
                return 0
            # If the rightmost characters of s and t match, increment the
            # match count and start searching from the next left character
            # of each string.
            if s[m - 1] == t[n - 1]:
                return 1 + findMatchCount(s, t, m-1, n-1)
            else:
                # If the rightmost characters of s and to do not match, then
                # shorten t by removing the rightmost character and start
                # searching the strings again.
                return findMatchCount(s, t, m, n-1)

        # s cannot be longer than t
        slen = len(s)
        tlen = len(t)
        if slen > tlen:
            return False
        if s == t:
            return True
        if findMatchCount(s, t, slen, tlen) == slen:
            return True
        else:
            return False


# Main section
sol = Solution()
for s, t, rslt in [
                     ('abc', 'ahbgdc', True),
                     ('axc', 'ahbgdc', False),
                     ('', 'ahbgdc', True),
                     ('abcd', '', False),
                     ('', '', True),
                     ('abcdef', 'abcdef', True),
                     ('abcdef', 'fedcba', False),
                     ('abcd', 'ab', False),
                     ('ab', 'baab', True),
                     ('rjufvjafbxnbgriwgokdgqdqewn', 'mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq', False),
                  ]:
    print(f's = {s} ; t = {t}')
    r = sol.isSubsequence(s, t)
    print(f'r = {r}')
    #assert r == rslt
    print('======================')


