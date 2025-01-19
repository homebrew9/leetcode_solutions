# 
# The intuition for this problem is as follows:
#     1) If the string length is odd, it can never have matched parentheses
#     2) Going from left to right, the count of ')' must never exceed the count of '('
#     3) Going from right to left, the count of '(' must never exceed the count of ')'
# Statements 2) and 3) are true because in the event of such a situation, we will have 
# no opportunity to "fix" the parentheses!
# So the logic is to just traverse left to right and sum all counts of unlocked and '('.
# We choose unlocked because it can be "changed", an unlocked character can be ')'.
# When we encounter a locked ')', we decrement the count and ensure that balance is >= 0.
# Then we apply the same logic going from right to left.
# 

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        open_count = 0
        for ch, lc in zip(s, locked):
            if lc == '0' or ch == '(':
                open_count += 1
            else:
                open_count -= 1
                if open_count < 0:
                    return False
        #print(f'open_count = {open_count}')
        closed_count = 0
        for ch, lc in zip(reversed(s), reversed(locked)):
            if lc == '0' or ch == ')':
                closed_count += 1
            else:
                closed_count -= 1
                if closed_count < 0:
                    return False
        #print(f'closed_count = {closed_count}')
        return True

# Main section
for s, locked in [
                    ('))()))' , '010100'),
                    ('()()'   , '0000'  ),
                    (')'      , '0'     ),
                    ('))()))' , '011010'),
                    ('())(()(()(()', '100011110110'),
                    ('()', '11'),
                    ('())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(', '100011110110011011010111100111011101111110000101001101001111'),
                 ]:
    print(f's, locked = {s}, {locked}')
    sol = Solution()
    r = sol.canBeValid(s, locked)
    print(f'r = {r}')
    print('====================')


