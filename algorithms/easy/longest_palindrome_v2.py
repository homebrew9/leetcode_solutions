from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Let's say the string s is: 'aaaabb'.
        # Since all occurrence counts are even, it is a palindrome. Max length = len(s).
        # Let s = 'aaaabbc'. One character occurs odd number of times. Max length = len(s).
        # Let s = 'aaaabbcd'. 2 characters occur odd number of times. Max length = len(s) - 1
        # Let s = 'aaaabbcde'. 3 characters occur odd number of times. Max length = len(s) - 2
        # Let s = 'aaaabbcdef'. 4 characters occur odd number of times. Max length = len(s) - 3
        # Let s = 'aaaabbcdefg'. 5 characters occur odd number of times. Max length = len(s) - 4
        #
        # What if 5 characters occur odd number of times, but that odd number is > 1 ?
        # Let s = 'aaaabbcccdddeeefffggg'. Still the max length = len(s) - 4. Because out of the
        # characters [c,d,e,f,g], we choose 1 as our palindrome "center" and discard 4. Here's
        # the longest palindrome: 'aaaabbcccddeeffgg' => we chose 'c' and discarded [d,e,f,g]
        #
        cntr = Counter(s)
        odds = sum([freq % 2 for _, freq in cntr.items()])
        if odds <= 1:
            return len(s)
        else:
            return len(s) - odds + 1

# Main section
for s in [
            'abccccdd',
            'a',
            'aaaabbbb',
            'aaaabbbccdef',
            'aa',
            'aab',
            'aabaac',
            'ccc',
            'ababababa',
            'aaabbb',
            'aaaaabbbbbcccccddddd',
         ]:
    sol = Solution()
    print(f's = {s}')
    r = sol.longestPalindrome(s)
    print(f'r = {r}')
    print('=====================')


