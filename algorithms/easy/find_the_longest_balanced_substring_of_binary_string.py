class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_len = 0
        in_block = False
        zeros, ones = 0, 0
        for i, ch in enumerate(s):
            if ch == '0':
                if not in_block:
                    in_block = True
                if i - 1 >= 0 and s[i-1] == '1':
                    max_len = max(max_len, 2*min(zeros, ones))
                    ones = 0
                    zeros = 0
                zeros += 1
            elif ch == '1':
                if in_block:
                    ones += 1
        max_len = max(max_len, 2*min(zeros, ones))
        return max_len

# Main section
for s in [
            '01000111',
            '00111',
            '111',
            '11001111101111010111001101001110100111111111110110',
            '1110111110011010100111010',
            '00100111110010011010011010101011011101101100110111',
            '10101001110100110000111000110011010101101101010010',
            '00010101000101110100110101011111011011000111001100',
            '11100111011110100001100110101010110101000000000010',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.findTheLongestBalancedSubstring(s)
    print(f'r = {r}')
    print('====================')


