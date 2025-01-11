#
# Time = O(n), Space = O(n)
#
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_string = ''
        marker = 0
        for ch in s[::-1]:
            if ch == '#':
                marker += 1
            elif marker > 0:
                marker -= 1
            elif marker == 0:
                new_string += ch
        print(new_string)
        size = len(new_string)
        marker = 0
        i = 0
        for ch in t[::-1]:
            if ch == '#':
                marker += 1
            elif marker > 0:
                marker -= 1
            elif marker == 0:
                if i >= size or ch != new_string[i]:
                    return False
                i += 1
        # It's possible that this a partial match. Return false
        # in that case; it must be a complete match.
        if i < size:
            return False
        else:
            return True

# Main section
for s, t in [
               ('ab#c', 'ad#c'),
               ('ab##', 'c#d#'),
               ('a#c', 'b'),
               ('a######', '####'),
               ('a###b###x', '####x'),
               ('abcdefghijkl######xyzz#', 'abcdefx#y#z#xyzpqr###'),
               ('bxu##tw', 'bxj###tw'),
               ('aaa###a', 'aaaa###a'),
            ]:
    print(f's = {s} ; t = {t}')
    sol = Solution()
    r = sol.backspaceCompare(s, t)
    print(f'r = {r}')
    print('==========================')



