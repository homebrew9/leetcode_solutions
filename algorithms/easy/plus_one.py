from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = list()
        carry_over = 0
        is_last = True
        for d in reversed(digits):
            elem = d + carry_over
            if is_last:
                elem += 1
                is_last = False
            q, r = divmod(elem, 10)
            res += [r]
            carry_over = q
        if carry_over > 0:
            res += [carry_over]
        return res[::-1]

    def plusOne_1(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int(''.join(map(str, digits)))+1)))

    def plusOne_2(self, digits: List[int]) -> List[int]:
        return [int(ch) for ch in str(int(''.join(str(d) for d in digits))+1)]

    def plusOne_3(self, digits: List[int]) -> List[int]:
        n = 0
        for d in digits:
            n = 10 * n + d
        n += 1
        res = list()
        while n > 0:
            q, r = divmod(n, 10)
            res += [r]
            n = q
        return res[::-1]

# Main section
for digits in [
                 [1,2,3],
                 [4,3,2,1],
                 [9],
                 [9,9,9,9,9,9,9,9,9,9,9,9],
                 [7,6,1,2,4,1,7,3,6,4,4,3,6,6,4,5,9,9,0,4,5,8,2,5,7,4,2,5,7,3,8,7,4,2,2,4,5,7,0,3,6,5,0,4,8,2,3,8,2,9],
              ]:
    print(f'digits = {digits}')
    sol = Solution()
    r = sol.plusOne(digits)
    r1 = sol.plusOne_1(digits)
    r2 = sol.plusOne_2(digits)
    r3 = sol.plusOne_3(digits)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print(f'r3 = {r3}')
    assert(r == r1 == r2 == r3)
    print('====================')



