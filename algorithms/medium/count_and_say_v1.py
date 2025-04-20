# Recursive version
#
# ======================================================= 
# Stefan Pochmann's solutions!!!
# ======================================================= 
# Solution 1 ... using a regular expression
# def countAndSay(self, n):
#     s = '1'
#     for _ in range(n - 1):
#         s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
#     return s
# 
# Solution 2 ... using a regular expression
# def countAndSay(self, n):
#     s = '1'
#     for _ in range(n - 1):
#         s = ''.join(str(len(group)) + digit
#                     for group, digit in re.findall(r'((.)\2*)', s))
#     return s
# 
# Solution 3 ... using groupby
# def countAndSay(self, n):
#     s = '1'
#     for _ in range(n - 1):
#         s = ''.join(str(len(list(group))) + digit
#                     for digit, group in itertools.groupby(s))
#     return s
#
# ======================================================= 
#
class Solution:
    def countAndSay(self, n: int) -> str:
        def say(num):
            s = ''
            cnt = 0
            prev = None
            for digit in num:
                if prev is None:
                    cnt = 1
                elif digit == prev:
                    cnt += 1
                else:
                    s += str(cnt) + prev
                    cnt = 1
                prev = digit
                #print(f'\tdigit = {digit}, cnt = {cnt}, s = {s}')
            #print(f'digit = {digit}, cnt = {cnt}, s = {s}')
            s += str(cnt) + digit
            return s

        def casHelper(n):
            if n == '1':
                return '1'
            return say(casHelper(str(int(n) - 1)))

        ans = casHelper(str(n))
        return ans

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            10,
            15,
            20,
            25,
            30,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.countAndSay(n)
    print(f'r = {r}')
    print('=================')


