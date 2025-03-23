class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        containers = maxWeight // w
        return min(n * n, containers)

# Main section
for n, w, maxWeight in [
                          (2, 3, 15),
                          (3, 5, 20),
                          (2, 1, 3),
                       ]:
    print(f'n, w, maxWeight = {n}, {w}, {maxWeight}')
    sol = Solution()
    r = sol.maxContainers(n, w, maxWeight)
    print(f'r = {r}')
    print('===================')

