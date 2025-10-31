class Solution:
    def scoreBalance(self, s: str) -> bool:
        arr = [ord(ch) - ord('a') + 1 for ch in s]
        total = sum(arr)
        curr_sum = 0
        for i in range(len(arr)-1):
            curr_sum += arr[i]
            if curr_sum == total - curr_sum:
                return True
        return False

# Main section
for s in [
            'adcb',
            'bace',
            'vjtbbvkjvrkkngjldtvdlrgshdtfuccnuuttmfhhxzeuhurexcrdvxwlpgpzdwdksmudxngnrxbrarbfvhcteftkdbnerthgxpup',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.scoreBalance(s)
    print(f'r = {r}')
    print('=====================')

