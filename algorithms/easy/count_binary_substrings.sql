class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        N = len(s)
        zeros, ones = 0, 0
        for i in range(N):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            if i < N - 1:
                if s[i] != s[i+1]:
                    res += min(zeros, ones)
                    if s[i+1] == '0':
                        zeros = 0
                    else:
                        ones = 0
            else:
                res += min(zeros, ones)
        return res

    def countBinarySubstrings_1(self, s: str) -> int:
        occur = list()
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                occur.append(cnt)
                cnt = 1
        occur.append(cnt)
        cnt = 0
        for i in range(1, len(occur)):
            cnt += min(occur[i-1], occur[i])
        return cnt

# Main section
for s in [
            '00110011',
            '10101',
            '0010111001011000110100010010001110011101101111000110100101000001000010001011101011001111111111001111',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.countBinarySubstrings(s)
    r1 = sol.countBinarySubstrings_1(s)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('=================================================')
 



