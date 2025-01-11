#
# Does not work!!
#
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        extra = 0
        while left <= right:
            #print(f'\tleft, right, c1, c2 = {left}, {right}, {s[left]}, {s[right]}')
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # This logic will not work! In the 2-pointer approach, if we hit a mismatch
                # we *CANNOT* "move left one place" or "move right one place". Consider:
                #     'aglcuffuculga'
                # 'agl' <=> 'lga' and then 'c' <> 'u'
                # We move 1 place from left => 'u' == 'u', but then 'f' <> 'c' and we incorrectly report this as False.
                # We should move 1 place from right in this case.
                # But then consider:
                #     'aglucuffuclga'
                # 'alg' <=> 'lga' and then 'u' <> 'c'.
                # We move 1 place from right => 'u' == 'u', but then 'c' <> 'f' and we incorrectly report this as False.
                # We should move 1 place from left in this case.
                # A better logic is to do this:
                # Upon mismatch:
                # a) take out the left char and check if the remaining string is a palindrome.
                # b) take out the right char and check if the remaining string is a palindrome.
                # If either a) or b) is True, then return True else False.

                #if s[left+1] == s[right]:
                #    extra += 1
                #    left += 1
                #    if extra > 1:
                #        return False
                #elif s[right-1] == s[left]:
                #    extra += 1
                #    right -= 1
                #    if extra > 1:
                #        return False
                if s[right-1] == s[left]:
                    extra += 1
                    right -= 1
                    if extra > 1:
                        return False
                elif s[left+1] == s[right]:
                    extra += 1
                    left += 1
                    if extra > 1:
                        return False
                else:
                    return False
        #print(f'extra = {extra}')
        if extra <= 1:
            return True
        return False

# Main section
for s in [
            #'a',
            #'aa',
            #'ab',
            #'aaa',
            #'aba',
            #'abca',
            #'abc',
            #'tebbem',
            #'abcdefedcba',
            #'abcddcba',
            #'abcdedcxba',
            #'abxcdedcba',
            #'abxycdedcba',
            #'abcdexfghijkjiyhgfedcba',
            'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.validPalindrome(s)
    print(f'r = {r}')
    print('===========================')


