class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # Bottom Up DP
        N = primeOne * primeTwo
        arr = [0 for _ in range(N)]
        for i in range(0, N):
            if i == 0 or arr[i] == 1:
                arr[i] = 1
                if i + primeOne < N:
                    arr[i + primeOne] = 1
                if i + primeTwo < N:
                    arr[i + primeTwo] = 1
        return max([i for i, v in enumerate(arr) if v == 0])

# Main section
for primeOne, primeTwo in [
                             (2, 5),
                             (5, 7),
                             (101, 103),
                             (269, 79),
                          ]:
    print(f'primeOne, primeTwo = {primeOne}, {primeTwo}')
    sol = Solution()
    r = sol.mostExpensiveItem(primeOne, primeTwo)
    print(f'r = {r}')
    print('==================')



