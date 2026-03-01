class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set([s[i-k+1:i+1] for i in range(k-1, len(s))])) == 2**k

# Main section
for s, k in [
               ('00110110', 2),
               ('0110', 1),
               ('0110', 2),
               ('1110101001011110110110000111010010101110111000101001110001100101001111110111110110011010011011011011', 3),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.hasAllCodes(s, k)
    print(f'r = {r}')
    print('=================================================')
 



