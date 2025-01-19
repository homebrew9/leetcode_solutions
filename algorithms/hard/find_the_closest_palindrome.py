import re
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def build_palindrome(root, is_even_length):
            # ('123', True)  = '123321'
            # ('123', False) = '12321'
            if is_even_length:
                return root + root[::-1]
            else:
                return root[:-1] + root[-1] + root[:-1][::-1]

        # Corner Cases
        # 1) n = 1,2,3,...,9,10, 100, 1000, 10000, ...
        if int(n) <= 10 or (n[0] == '1' and int(n[1:]) == 0):
            return str(int(n) - 1)
        # 2) n = 11, 101, 1001, 10001, ...
        if n[0] == '1' and n[-1] == '1' and (n[1:-1] == '' or int(n[1:-1]) == 0):
            return str(int(n) - 2)
        # 3) n = 99, 999, 9999, 99999, ....
        if re.match('^9+$', n):
            return str(int(n) + 2)

        N = len(n)
        is_even_length = (N % 2 == 0)
        if is_even_length:
            root = n[:N//2]
        else:
            root = n[:N//2 + 1]
        # Create a palindrom and check the diff
        ans = build_palindrome(root, is_even_length)
        diff = int(ans) - int(n)
        if diff < 0:
            # 1st palindrome < n, increase it to find the 2nd palindrome
            ans1 = ans
            root = str(int(root) + 1)
            ans2 = build_palindrome(root, is_even_length)
        elif diff > 0:
            # 1st palindrome > n, decrease it to find the 2nd palindrome
            ans1 = ans
            root = str(int(root) - 1)
            ans2 = build_palindrome(root, is_even_length)
        else:
            # n itself is a palindrome, find lower and higher palindromes
            root1 = str(int(root) - 1)
            ans1 = build_palindrome(root1, is_even_length)
            root2 = str(int(root) + 1)
            ans2 = build_palindrome(root2, is_even_length)
        diff1 = abs(int(ans1) - int(n))
        diff2 = abs(int(ans2) - int(n))
        if diff1 < diff2:
            return ans1
        elif diff2 < diff1:
            return ans2
        else:
            min_ans = min(int(ans1), int(ans2))
            return str(min_ans)

# Main section
for n, ans in [
                 ('123',                '121'           ),
                 ('1',                  '0'             ),
                 ('374952831',          '374949473'     ),
                 ('37492831',           '37488473'      ),
                 ('8888',               '8778'          ),
                 ('1111',               '1001'          ),
                 ('11',                 '9'             ),
                 ('100',                '99'            ),
                 ('101',                '99'            ),
                 ('1001',               '999'           ),
                 ('10001',              '9999'          ),
                 ('100001',             '99999'         ),
                 ('1000001',            '999999'        ),
                 ('10000001',           '9999999'       ),
                 ('100000001',          '99999999'      ),
                 ('1000000001',         '999999999'     ),
                 ('10000000001',        '9999999999'    ),
                 ('100000000001',       '99999999999'   ),
                 ('1000000000001',      '999999999999'  ),
                 ('10000000000001',     '9999999999999' ),
                 ('88',                 '77'            ),
                 ('9',                  '8'             ),
              ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.nearestPalindromic(n)
    print(f'r = {r}')
    assert(r == ans)
    print('==================================')


