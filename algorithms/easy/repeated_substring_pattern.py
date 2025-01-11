# I need to work more on this logic. It seems within grasp, but I can't
# seem to figure it out. This code fails for the last two test cases.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s1 = s[l]
        s2 = s[r]
        while True:
            if l > r:
                return False
            elif l == r - 1:
                if s1 == s2:
                    return True
                else:
                    return False
            else:
                if s1 == s2:
                    mid = s[l+1:r]
                    print(f'\t>>> mid = [{mid}]')
                    if len(mid) == 0:
                        return True
                    elif s1 == mid:
                        return True
                    else:
                        return self.repeatedSubstringPattern(mid)
            l += 1
            r -= 1
            s1 += s[l]
            s2 = s[r] + s2

# Main section
for s in [
            #'abcdefghijabcdefghij',
            #'abcdabcdabcbbcabcdabcd',
            #'abcdabcdabcd',
            #'abcabcabcabc',
            #'a',
            #'aa',
            #'ab',
            #'abc',
            'aba',  # Fails: it should return False instead of True!
            #'abcdefdefabc',
         ]:
    sol = Solution()
    print(f's = {s}')
    r = sol.repeatedSubstringPattern(s)
    print(f'r = {r}')
    print('==========================')

