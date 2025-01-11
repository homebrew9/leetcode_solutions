#
# https://leetcode.com/problems/buddy-strings/discuss/141780/Easy-Understood
# Very good explanation
#
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # If lengths are different then no swap is possible
        if len(s) != len(goal):
            return False
        # If strings are identical and there are repeated chars
        # in s then swap is possible
        if s == goal and len(set(s)) < len(s):
            return True
        # If all chars in s and goal are different, then collect
        # distinct character-pairs iterating through s and goal.
        # If a) no. of such character-pairs is 2, and
        #    b) 2nd pair, when reversed, equals 1st pair,
        # then swap is possible
        diff = list()
        for a, b in zip(s, goal):
            if a != b:
                diff.append((a, b))
        if len(diff) == 2 and diff[0] == diff[1][::-1]:
            return True
        else:
            return False

# Main section
sol = Solution()
for s, goal in [
                  ('ab', 'ba'),
                  ('ab', 'ab'),
                  ('aa', 'aa'),
                  ('abcdefghij', 'abcdjfghie'),
                  ('abcdea', 'abcdea'),
                  ('abcdefga', 'abcgefda'),
                  ('abcdefghij', 'jbchefgdia'),
                  ('abcdef', 'abcxyz'),
                  ('abcdef', 'abxdey'),
               ]:
    print(f's = {s} ; goal = {goal}')
    r = sol.buddyStrings(s, goal)
    print(f'r = {r}')
    print('======================')

