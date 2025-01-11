class Solution:
    def hammingWeight(self, n: int) -> int:
        #bin_num = bin(n)
        #retval = str(bin_num).replace('0b','')
        #retval = retval.replace('0','')
        #return len(retval)
        return len(str(bin(n)).replace('0b','').replace('0',''))

# Main section
sol = Solution()
for n in [
            0b00000000000000000000000000001011,
            0b00000000000000000000000010000000,
            0b11111111111111111111111111111101,
         ]:
    print(f'n = {bin(n)}')
    r = sol.hammingWeight(n)
    print(f'r = {r}')
    print('===========================')


