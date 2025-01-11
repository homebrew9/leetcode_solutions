class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # A subsequence of a string 'abc' is any one in this list:
        # ('', 'a', 'b', 'c', 'ab', 'bc', 'ac', 'abc')
        # So if two strings are different (irrespective of any common chars),
        # say 'abcdef' and 'pqarsbtev' then the LONGER string is a
        # subsequence NOT found in the smaller string! The rest is easy.
        # a) Strings are identical => return -1
        # b) Strings are non-identical but length is same then return either length.
        # c) Strings are non-identical and lengths are different, then return greater length.
        # Looks like b) and c) can be combined - just return max of two lengths!

        #if a == b:
        #    return -1
        #elif len(a) == len(b) and a != b:
        #    return len(a)
        #else:
        #    return max(len(a), len(b))

        if a == b:
            return -1
        return max(len(a), len(b))

# Main section
for a, b in [
               ('aba', 'cdc'),
               ('abcdef', 'pqarsbtev'),
               ('aaa', 'aaa'),
            ]:
    print(f'a = {a}, b = {b}')
    sol = Solution()
    r = sol.findUSlength(a, b)
    print(f'r = {r}')
    print('===========================')

