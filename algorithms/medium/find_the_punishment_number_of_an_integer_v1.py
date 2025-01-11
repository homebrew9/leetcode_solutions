#
# Recursive function that does not write to a global variable.
#
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canBePartitioned(num_str, total, num):
            #print(f'\tnum_str, total = {num_str}, {total}')
            if num_str == '':
                return total == num
            for i in range(1, len(num_str)+1):
                ret = canBePartitioned(num_str[i:], total + int(num_str[:i]), num)
                if ret:
                    return True
            return False
        res = 0
        for num in range(1, n+1):
            if canBePartitioned(str(num*num), 0, num):
                #print(f'in if; num, num*num = {num}, {num*num}')
                res += num*num
        return res

# Main section
for n in [
            7,
            10,
            37,
            123,
            679,
            1000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.punishmentNumber(n)
    print(f'r = {r}')
    print('=========================')


