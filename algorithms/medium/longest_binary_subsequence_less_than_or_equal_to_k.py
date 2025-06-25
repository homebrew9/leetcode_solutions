class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        N = len(s)
        place_value = 1
        num = 0
        res = 0
        is_num_greater = False
        i = N - 1
        while i >= 0:
            if is_num_greater:
                if s[i] == '0':
                    res += 1
            else:
                num += int(s[i]) * place_value
                if num > k:
                    is_num_greater = True
                else:
                    res += 1
                    place_value *= 2
            i -= 1
        return res

# Main section
for s, k in [
               ('1001010', 5),
               ('00101001', 1),
               ('0111101000101000110101011000011101111001010100100111101001001101001011010101011111111110101100010111', 103),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.longestSubsequence(s, k)
    print(f'r = {r}')
    print('=======================')























