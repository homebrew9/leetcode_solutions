class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        arr = perm[:]
        steps = 0
        while True:
            arr = [arr[i//2] if i % 2 == 0 else arr[n//2 + (i-1)//2] for i in range(n)]
            steps += 1
            if arr == perm:
                return steps

# Main section
for n in [
               2,
               4,
               6,
               8,
              10,
              72,
             100,
             598,
             900,
            1000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.reinitializePermutation(n)
    print(f'r = {r}')
    print('================')

