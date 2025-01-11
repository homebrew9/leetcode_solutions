import re

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Use the regex ".{1,k}" to match any character of length 1 to k
        # Double braces are used to escape braces in Python f-strings
        fmt = f'.{{1,{k}}}'

        # Split the string s into chunks of length k each. The length
        # of last chunk may be less than k.
        arr = re.findall(fmt, s)

        # Reverse every alternate chunk in the array arr
        arr1 = [v[::-1] if i % 2 == 0 else v for i, v in enumerate(arr)]

        # Join back to a string and return
        return ''.join(arr1)

# Main section
for s, k in [
               ('abcdefg', 2),
               ('abcd', 2),
               ('abcdefghijklmnopqrstuvwxyz', 3),
               ('a', 1),
               ('ab', 1),
               ('abcd', 1),
               ('abcde', 1),
               ('abcdefg', 1),
               ('a', 5),
               ('ab', 5),
               ('abcde', 5),
               ('abcdef', 5),
               ('abcdefg', 5),
               ('abcdefgh', 5),
               ('abcdefghi', 5),
               ('abcdefghij', 5),
               ('abcdefghijk', 5),
            ]:
    print(f's = {s}, k = {k}')
    sol = Solution()
    r = sol.reverseStr(s, k)
    print(f'r = {r}')
    print('===========================')


