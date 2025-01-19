#
# Excellent explanation in the Discussion section here:
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/discuss/5818284/Sliding-Window-with-Example-Walkthrough
# The code here works for the Hard version of this problem too:
# 3298: Count substrings that can be rearranged to contain a string II
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/
#

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        arr1 = [0 for _ in range(26)]
        arr2 = [0 for _ in range(26)]
        for ch in word2:
            arr2[ord(ch) - 97] += 1
        #print(f'arr2 = {arr2}')
        k = len(word2)
        N = len(word1)
        res = 0
        i, j = 0, 0
        while j < N:
            ch = word1[j]
            if arr1[ord(ch) - 97] < arr2[ord(ch) - 97]:
                k -= 1
            arr1[ord(ch) - 97] += 1
            #print(f'j, ch, arr1, k = {j}, {ch}, {arr1}, {k}')
            if k == 0:
                # We have a substring that contains word2
                res += (N - j)
                #print(f'\tk, res = {k}, {res}')
                # Now shrink the sliding window
                while i <= j:
                    i += 1
                    v = word1[i-1]
                    arr1[ord(v) - 97] -= 1
                    if arr2[ord(v) - 97] > arr1[ord(v) - 97]:
                        k += 1
                    if k == 0:
                        res += (N - j)
                    if arr1[ord(v) - 97] < arr2[ord(v) - 97]:
                        break
            j += 1
        return res

# Main section
for word1, word2 in [
                       ('bcca', 'abc'),
                       ('abcabc', 'abc'),
                       ('abcabc', 'aaabc'),
                       ('bbbb', 'b'),
                       ('dcbdcdccb', 'cdd'),
                    ]:
    print(f'word1, word2 = {word1}, {word2}')
    sol = Solution()
    r = sol.validSubstringCount(word1, word2)
    print(f'r = {r}')
    print('==================')


