class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for n in range(low, high + 1):
            arr = list(str(n))
            if len(arr) % 2 == 0 and sum([int(x) for x in arr[:len(arr)//2]]) == sum([int(x) for x in arr[len(arr)//2:]]):
                res += 1
        return res

# Main section
for low, high in [
                    (1, 100),
                    (1200, 1230),
                 ]:
    print(f'low, high = {low}, {high}')
    sol = Solution()
    r = sol.countSymmetricIntegers(low, high)
    print(f'r = {r}')
    print('========================')

