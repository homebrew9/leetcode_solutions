#
# Check the section on Edit Distance in Dynamic Programming in the book
# Algorithms by Dasgupta, Papadimitrou, Vazirani
#

def editDistance(s1, s2):
    M = len(s1)
    N = len(s2)
    dp = [[None for _ in range(M+1)] for _ in range(N+1)]
    for c in range(M+1):
        dp[0][c] = c
    for r in range(N+1):
        dp[r][0] = r
    for r in range(1, N+1):
        for c in range(1, M+1):
            dp[r][c] = min(1 + dp[r-1][c],
                           1 + dp[r][c-1],
                           (0 if s2[r-1] == s1[c-1] else 1) + dp[r-1][c-1])
    #print(f'\tdp = {dp}')
    return dp[N][M]

# Main section
for s1, s2 in [
                 ('polynomial', 'exponential'),
                 ('sunny', 'snowy'),
                 ('thequickbrownfox', 'thequickbrownfox'),
                 ('helloworld', 'dlrowolleh'),
                 ('dlrowolleh', 'helloworld'),
                 ('nowisthetimeforallyoungmen', 'thewoodsarelovelydarkanddeep'),
              ]:
    print(f's1, s2 = {s1}, {s2}')
    r = editDistance(s1, s2)
    print(f'r = {r}')
    print('================')

