from typing import List

class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        arr = list(range(n, 0, -1))
        S = sum(arr)
        #print(f'arr, S, target = {arr}, {S}, {target}')
        # If S is an odd integer, then we can reach all targets 1,3,5,...,S
        # by summation of a permutation of n. We cannot reach an even number though.
        # Similarly, if S is an even integer, then we can reach all targets 0,2,4,...S
        # by summation of a permutation of n. We cannot reach an odd number though.
        # I don't know if this is some theorem in Mathematics, or what the proof is.
        if target < -S or target > S or (S - target) % 2 == 1:
            return []
        D = S - target
        # Flipping x to -x reduces the sum by 2*x
        for i in range(len(arr)):
            #print(f'\ti, arr[i], D, arr = {i}, {arr[i]}, {D}, {arr}')
            if 2*arr[i] <= D:
                D -= 2*arr[i]
                arr[i] = -arr[i]
        return sorted(arr)

# Main section
for n, target in [
                    (3, 0),
                    (1, 10000000000),
                    (100000, 5000049999),
                    (1, 0),
                    (5, 9),
                 ]:
    print(f'n, target = {n}, {target}')
    sol = Solution()
    r = sol.lexSmallestNegatedPerm(n, target)
    print(f'r = {r}')
    print('===========================')







