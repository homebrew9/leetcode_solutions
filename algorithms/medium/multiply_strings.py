class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def partialProduct(s, d, arr):
            digits = [int(i) for i in s]
            d = int(d)
            carry_over = 0
            for i in digits:
                product = i*d + carry_over
                p, q = divmod(product, 10)
                arr.append(q)
                carry_over = p
            if carry_over > 0:
                arr.append(carry_over)
            res = 0
            for i in arr[::-1]:
                res = 10 * res + i
            return res

        total = 0
        for i, v in enumerate(num2[::-1]):
            total += partialProduct(num1[::-1], v, [0]*i)
        return str(total)

# Main section
for num1, num2 in [
                    ('123','456'),
                    ('2','3'),
                    ('123456789','987654321'),
                    ('1234567891234567891234567891234567891234567890','9876543210987654321098765432109876543210987654321'),
                  ]:
    print(f'num1, num2 = {num1}, {num2}')
    sol = Solution()
    r = sol.multiply(num1, num2)
    print(f'r = {r}')
    print('===========================')

