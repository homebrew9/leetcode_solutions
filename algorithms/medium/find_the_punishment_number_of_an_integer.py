#
# In the solution below, the recursive function is writing to a global variable. Can the
# global variable be avoided? Version 1 is an attempt to return True/False from the recursive
# function itself without the need for a global variable.
#
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canBePartitioned(num_str, arr):
            if num_str == '':
                res.append(arr)
                return
            for i in range(1, len(num_str)+1):
                canBePartitioned(num_str[i:], arr + [num_str[:i]])
        ans = 0
        for num in range(1, n+1):
            res = list()
            canBePartitioned(str(num*num), [])
            #print(f'\tres = {res}')
            for x in res:
                if sum([int(y) for y in x]) == num:
                    #print(f'\t\tnum, num*num = {num}, {num*num}')
                    ans += num*num
                    break
        return ans

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

