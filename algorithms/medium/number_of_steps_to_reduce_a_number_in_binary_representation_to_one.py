class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Process from right to left (skip first bit since we stop at "1")
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry
            
            if bit % 2 == 1:  # Odd: need to add 1
                steps += 2      # +1 for add, +1 for divide
                carry = 1       # Adding 1 to odd creates carry
            else:               # Even: just divide
                steps += 1
        
        return steps + carry  # Final carry means one more add operation

# Main section
for s in [
            '1101',
            '10',
            '1',
            '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
            '100',
            '11111',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.numSteps(s)
    print(f'r = {r}')
    print('=================================================')
 





