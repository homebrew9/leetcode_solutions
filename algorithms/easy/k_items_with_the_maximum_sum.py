class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        arr = [1 for _ in range(numOnes)] + [0 for _ in range(numZeros)] + [-1 for _ in range(numNegOnes)]
        print(f'\tarr = {arr}')
        return sum(arr[:k])

# Main section
for numOnes, numZeros, numNegOnes, k in [
                                           (3, 2, 0, 2),
                                           (3, 2, 0, 4),
                                        ]:
    print(f'numOnes, numZeros, numNegOnes, k = {numOnes}, {numZeros}, {numNegOnes}, {k}')
    sol = Solution()
    r = sol.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)
    print(f'r = {r}')
    print('================')

