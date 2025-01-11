#
# From the Solution section. Good logic and use of generator!
# Space Complexity = O(1)
# Time Complexity = O(M + N), where M, N are the lengths of s, t
#
import itertools

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parse(m):
            skip = 0
            # If character is '#' (backspace) then increment skip
            # Then at the next character, decrement skip
            # Otherwise, return the character. This works because
            # we are traversing the string from right to left!
            for ch in reversed(m):
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield ch

        return all(x == y for x, y in itertools.zip_longest(parse(s), parse(t)))

# Main section
for s, t in [
               ('ab#c', 'ad#c'),
               ('ab##', 'c#d#'),
               ('a#c', 'b'),
               ('a######', '####'),
               ('a###b###x', '####x'),
            ]:
    print(f's = {s} ; t = {t}')
    sol = Solution()
    r = sol.backspaceCompare(s, t)
    print(f'r = {r}')
    print('==========================')


