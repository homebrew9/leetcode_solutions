class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(list(n)))

# Main section
for n in [
            '32',
            '82734',
            '27346209830709182346',
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.minPartitions(n)
    print(f'r = {r}')
    print('=================================================')
 













