class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        def get_index(ch):
            return ord(ch) - ord('a')

        N = len(s)
        if k > N:
            return 0
        arr = [0 for _ in range(26)]
        res = 0
        for i in range(0, N-k+1):
            if i == 0:
                j = 0
                while j < k:
                    arr[get_index(s[j])] += 1
                    j += 1
            else:
                arr[get_index(s[i-1])] -= 1
                arr[get_index(s[i+k-1])] += 1
            if sum(1 for x in arr if x > 1) == 0:
                res += 1
        return res

# Main section
for s, k in [
               ('havefunonleetcode', 5),
               ('home', 5),
               ('ddddgffejaebjajjcifibfbaegddbaegihhhgcjhdadfgfghjgchjefcadfgcdfbgacaiiabjibbjehecaihghjfeebceihciibc', 100)
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.numKLenSubstrNoRepeats(s, k)
    print(f'r = {r}')
    print('=======================')

