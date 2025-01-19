class Solution:
    def findContestMatch(self, n: int) -> str:
        def solve(arr):
            if len(arr) == 1:
                return arr[0]
            arr = [f'({arr[i]},{arr[len(arr)-1-i]})' for i in range(len(arr)//2)]
            return solve(arr)
        return solve([i for i in range(1, n+1)])

# Main section
for n in [
            2,
            4,
            8,
            16,
            32,
            64,
            128,
            256,
            512,
            #1024,
            #2048,
            #4096,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.findContestMatch(n)
    print(f'r = {r}')
    print('========================')

