# =========================================================================================================
# CSES.fi => coin combination
# You are given infinite coins of denominations {1,3,4}. Given a number n, return the minimum number
# of coins needed to add up to n. E.g.
# If n = 6 => return 2, since 3+3 = 6 and 2 is the minimum number of coins.
# If n = 10 => return 3, since 3+3+4 = 10 and 3 is the minimum number of coins.
# =========================================================================================================


def minimumCoins(arr, n):
    def solve(n):
        if n < 0:
            return float('inf')
        if n == 0:
            return 0
        best = float('inf')
        for c in arr:
            best = min(best, solve(n - c) + 1)
        return best

    # Recursive solution - very inefficient for large n
    return solve(n)

def minimumCoins1(arr, n):
    def solve(n):
        if n in hsh:
            return hsh[n]
        if n < 0:
            hsh[n] = float('inf')
            return hsh[n]
        if n == 0:
            hsh[n] = 0
            return hsh[n]
        best = float('inf')
        for c in arr:
            best = min(best, solve(n - c) + 1)
        hsh[n] = best
        return hsh[n]

    # Memoized recursive solution
    hsh = dict()
    ret = solve(n)
    #print(f'\thsh = {hsh}')
    return ret

def minimumCoins2(arr, n):
    def solve(n):
        for i in range(1, n+1):
            hsh[i] = min(hsh[i-1]+1, hsh[i-3]+1, hsh[i-4]+1)
        return hsh[n]

    # Iterative solution
    hsh = dict()
    for i in range(-4, 0):
        hsh[i] = float('inf')
    hsh[0] = 0
    ret = solve(n)
    #print(f'\thsh = {hsh}')
    return ret


# Main section
for arr, n in [
                 ([1,3,4], 5),
                 ([1,3,4], 10),
                 ([1,3,4], 30),
                 ([1,3,4], 100),
                 ([1,3,4], 987),
                 ([1,3,4], 3599),
                 ([1,3,4], 10234),
              ]:
    print(f'arr, n = {arr}, {n}')
    #r = minimumCoins(arr, n)
    #r = minimumCoins1(arr, n)
    r = minimumCoins2(arr, n)
    print(f'r = {r}')
    print('===============')

