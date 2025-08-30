class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Alice wins if total number of flowers is odd.
        # odd + odd = even
        # odd + even = odd   <==
        # even + odd = odd   <==
        # even + even = even
        # n = 3, m = 2
        # n = [1,3] ; m = [2] => 2 * 1 = 2
        # n = [2]   ; m = [1] => 1 * 1 = 1  => Total = 2 + 1 = 3
        # Given an integer, say n, can you find out:
        #   1) the number of odd integers in the range [1, n] ?
        #   2) the number of even integers in the range [1, n] ?
        # That depends on the parity of n.
        # If n is even => n//2 odds and n//2 evens in [1, n]
        # If n is odd  => n//2 + 1 odds and n//2 evens in [1, n]
        res = 0
        if n % 2 == 0 and m % 2 == 0:
            # Both n and m are even : O(n) * E(m) + E(n) * O(m)
            res = (n//2) * (m//2) + (n//2) * (m//2)
        elif n % 2 == 0 and m % 2 == 1:
            # n is even and m is odd : O(n) * E(m) + E(n) * O(m)
            res = (n//2) * (m//2) + (n//2) * (m//2 + 1)
        elif n % 2 == 1 and m % 2 == 0:
            # n is odd and m is even : O(n) * E(m) + E(n) * O(m)
            res = (n//2 + 1) * (m//2) + (n//2) * (m//2)
        else:
            # Both n and m are odd : O(n) * E(m) + E(n) * O(m)
            res = (n//2 + 1) * (m//2) + (n//2) * (m//2 + 1)
        return res

# Main section
for n, m in [
               (3, 2),
               (1, 1),
               (20563, 60472),
               (48107, 52061),
            ]:
    print(f'n, m = {n}, {m}')
    sol = Solution()
    r = sol.flowerGame(n, m)
    print(f'r  = {r}')
    print('===================')




