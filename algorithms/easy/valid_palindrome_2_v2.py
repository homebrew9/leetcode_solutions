class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            lft = 0
            rgt = len(s) - 1
            while lft < rgt:
                if s[lft] != s[rgt]:
                    return False
                lft += 1
                rgt -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Now the left and right chars don't match. So we take out the left and right
                # char one after the another and check if the remaining string is a palindrome.
                # If it is a palindrome in either case we return True else False.
                rem1 = s[left+1:right+1] # remove left char and grab the string in between
                rem2 = s[left:right]     # remove right char and grab the string in between
                if isPalindrome(rem1) or isPalindrome(rem2):
                    return True
                else:
                    return False
        # we have traversed through the entire string and it is a palindrome
        return True

# Main section
for s in [
            'a',
            'aa',
            'ab',
            'aaa',
            'aba',
            'abca',
            'abc',
            'tebbem',
            'abcdefedcba',
            'abcddcba',
            'abcdedcxba',
            'abxcdedcba',
            'abxycdedcba',
            'abcdexfghijkjiyhgfedcba',
            'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.validPalindrome(s)
    print(f'r = {r}')
    print('===========================')



