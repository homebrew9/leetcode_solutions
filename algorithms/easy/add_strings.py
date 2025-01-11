class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = num2.zfill(len(num1))
        elif len(num2) > len(num1):
            num1 = num1.zfill(len(num2))
        #print(f'\tnum1 = {num1}, num2 = {num2}')
        res = ''
        add, carry = 0, 0
        for a, b in zip(num1[::-1], num2[::-1]):
            add = int(a) + int(b) + carry
            res += str(add % 10)
            carry = add // 10
        if carry > 0:
            res += str(carry)
        return res[::-1]

# Main section
for num1, num2 in [
                       ('11', '123'),
                       ('456', '777'),
                       ('456', '77'),
                       ('0', '0'),
                       ('123456789', '987654321'),
                       ('99999999999', '9999999999999'),
                       ('12981278483743987397298427394827394823749823749237492729742974923742397429', '998237283729298739729372983729372937293729372973297302387938329323928732989'),
                  ]:
    sol = Solution()
    print(f'num1 = {num1}, num2 = {num2}')
    r = sol.addStrings(num1, num2)
    print(f'r = {r}')
    assert int(r) == int(num1) + int(num2)
    print('==========================')

